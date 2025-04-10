# Testing Your Database

To ensure that queries return the expected data, RLS policies are correctly applied, and everything works as expected, we encourage you to write automated tests. There are essentially two approaches to testing:

1. Write tests that interface with a Supabase client instance (same way you use Supabase client in your application code) in the programming language(s) you use in your application and using your favorite testing framework.

2. Test through the Supabase CLI, which is a more low-level approach where you write tests in SQL.

## Testing using the Supabase CLI

You can use the Supabase CLI to test your database. The minimum required version of the CLI is [v1.11.4](https://github.com/supabase/cli/releases). To get started:

- [Install the Supabase CLI](https://supabase.com/docs/guides/cli) on your local machine

### Creating a test

Create a tests folder inside the `supabase` folder:

```bash
mkdir -p ./supabase/tests/database
```

Create a new file with the `.sql` extension which will contain the test:

```bash
touch ./supabase/tests/database/hello_world.test.sql
```

### Writing tests

All `sql` files use [pgTAP](https://supabase.com/docs/guides/database/extensions/pgtap) as the test runner.

Let's write a simple test to check that our `auth.users` table has an ID column. Open `hello_world.test.sql` and add the following code:

```sql
begin;
select plan(1); -- only one statement to run

SELECT has_column(
    'auth',
    'users',
    'id',
    'id should exist'
);

select * from finish();
rollback;
```

### Running tests

To run the test, you can use:

```bash
supabase test db
```

This will produce the following output:

```
$ supabase test db
supabase/tests/database/hello_world.test.sql .. ok
All tests successful.
Files=1, Tests=1,  1 wallclock secs ( 0.01 usr  0.00 sys +  0.04 cusr  0.02 csys =  0.07 CPU)
Result: PASS
```

## More resources

- [Testing RLS policies](https://supabase.com/docs/guides/database/extensions/pgtap#testing-rls-policies)
- [pgTAP extension](https://supabase.com/docs/guides/database/extensions/pgtap)
- Official [pgTAP documentation](https://pgtap.org/)
