# Debugging Performance Issues

## Debug slow-running queries using the Postgres execution planner

`explain()` is a method that provides the Postgres `EXPLAIN` execution plan of a query. It is a powerful tool for debugging slow queries and understanding how Postgres will execute a given query. This feature is applicable to any query, including those made through `rpc()` or write operations.

## Enabling `explain()`

`explain()` is disabled by default to protect sensitive information about your database structure and operations. We recommend using `explain()` in a non-production environment. Run the following SQL to enable `explain()`:

```sql
-- enable explain
alter role authenticator
set pgrst.db_plan_enabled to 'true';

-- reload the config
notify pgrst, 'reload config';
```

## Using `explain()`

To get the execution plan of a query, you can chain the `explain()` method to a Supabase query:

```javascript
const { data, error } = await supabase
  .from('instruments')
  .select()
  .explain()
```

### Example data

To illustrate, consider the following setup of a `instruments` table:

```sql
create table instruments (
  id int8 primary key,
  name text
);

insert into instruments
  (id, name)
values
  (1, 'violin'),
  (2, 'viola'),
  (3, 'cello');
```

### Expected response

The response would typically look like this:

```
Aggregate  (cost=33.34..33.36 rows=1 width=112)
  ->  Limit  (cost=0.00..18.33 rows=1000 width=40)
        ->  Seq Scan on instruments  (cost=0.00..22.00 rows=1200 width=40)
```

By default, the execution plan is returned in TEXT format. However, you can also retrieve it as JSON by specifying the `format` parameter.

## Production use with pre-request protection

If you need to enable `explain()` in a production environment, ensure you protect your database by restricting access to the `explain()` feature. You can do so by using a pre-request function that filters requests based on the IP address:

```sql
create or replace function filter_plan_requests()
returns void as $$
declare
  headers   json := current_setting('request.headers', true)::json;
  client_ip text := coalesce(headers->>'cf-connecting-ip', '');
  accept    text := coalesce(headers->>'accept', '');
  your_ip   text := '123.123.123.123'; -- replace this with your IP
begin
  if accept like 'application/vnd.pgrst.plan%' and client_ip != your_ip then
    raise insufficient_privilege using
      message = 'Not allowed to use application/vnd.pgrst.plan';
  end if;
end;
$$ language plpgsql;

alter role authenticator set pgrst.db_pre_request to 'filter_plan_requests';
notify pgrst, 'reload config';
```

Replace `'123.123.123.123'` with your actual IP address.

## Disabling explain

To disable the `explain()` method after use, execute the following SQL commands:

```sql
-- disable explain
alter role authenticator
set pgrst.db_plan_enabled to 'false';

-- if you used the above pre-request
alter role authenticator
set pgrst.db_pre_request to '';

-- reload the config
notify pgrst, 'reload config';
```
