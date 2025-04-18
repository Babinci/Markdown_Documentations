# Query Optimization

## Choosing indexes to improve your query performance

When working with Postgres, or any relational database, indexing is key to improving query performance. Aligning indexes with common query patterns can speed up data retrieval by an order of magnitude.

This guide is intended to:

- Help identify parts of a query that have the potential to be improved by indexes
- Introduce tooling to help identify useful indexes

This is not a comprehensive resource, but rather a helpful starting point for your optimization journey.

If you're new to query optimization, you may be interested in [`index_advisor`](https://supabase.com/docs/guides/database/extensions/index_advisor), our tool for automatically detecting indexes that improve performance on a given query.

## Example Query

Consider the following example query that retrieves customer names and purchase dates from two tables:

```sql
select
  a.name,
  b.date_of_purchase
from
  customers as a
  join orders as b on a.id = b.customer_id
where a.sign_up_date > '2023-01-01' and b.status = 'shipped'
order by b.date_of_purchase
limit 10;
```

In this query, there are several parts that indexes could likely help in optimizing the performance:

### `where` clause

The `where` clause filters rows based on certain conditions, and indexing the columns involved can improve this process:

- `a.sign_up_date`: If filtering by `sign_up_date` is common, indexing this column can speed up the query.
- `b.status`: Indexing the status may be beneficial if the column has diverse values.

```sql
create index idx_customers_sign_up_date on customers (sign_up_date);
create index idx_orders_status on orders (status);
```

### `join` columns

Indexes on the columns used for joining tables can help Postgres avoid scanning tables in their entirety when connecting tables.

- Indexing `a.id` and `b.customer_id` would likely improve the performance of the join in this query.
- Note that if `a.id` is the primary key of the `customers` table it is already indexed

```sql
create index idx_orders_customer_id on orders (customer_id);
```

### `order by` clause

Sorting can also be optimized by indexing:

- An index on `b.date_of_purchase` can improve the sorting process, and is particularly beneficial when a subset of rows is being returned with a `limit` clause.

```sql
create index idx_orders_date_of_purchase on orders (date_of_purchase);
```

## Key Concepts

Here are some concepts and tools to keep in mind to help you identify the best index for the job, and measure the impact that your index had:

### Analyze the query plan

Use the `explain` command to understand the query's execution. Look for slow parts, such as Sequential Scans or high cost numbers. If creating an index does not reduce the cost of the query plan, remove it.

For example:

```sql
explain select * from customers where sign_up_date > 25;
```

### Use appropriate index types

Postgres offers various index types like [B-tree, Hash, GIN, etc](https://www.postgresql.org/docs/current/indexes-types.html). Select the type that best suits your data and query pattern. Using the right index type can make a significant difference. For example, using a BRIN index on a field that always increases and lives within a table that updates infrequently - like `created_at` on an `orders` table - routinely results in indexes that are +10x smaller than the equivalent default B-tree index. That translates into better scalability.

```sql
create index idx_orders_created_at ON customers using brin(created_at);
```

### Partial indexes

For queries that frequently target a subset of data, a partial index could be faster and smaller than indexing the entire column. A partial index contains a `where` clause to filter the values included in the index. Note that a query's `where` clause must match the index for it to be used.

```sql
create index idx_orders_status on orders (status)
where status = 'shipped';
```

### Composite indexes

If filtering or joining on multiple columns, a composite index prevents Postgres from referring to multiple indexes when identifying the relevant rows.

```sql
create index idx_customers_sign_up_date_priority on customers (sign_up_date, priority);
```

### Over-Indexing

Avoid the urge to index columns you operate on infrequently. While indexes can speed up reads, they also slow down writes, so it's important to balance those factors when making indexing decisions.

### Statistics

Postgres maintains a set of statistics about the contents of your tables. Those statistics are used by the query planner to decide when it's is more efficient to use an index vs scanning the entire table. If the collected statistics drift too far from reality, the query planner may make poor decisions. To avoid this risk, you can periodically `analyze` tables.

```sql
analyze customers;
```

By following this guide, you'll be able to discern where indexes can optimize queries and enhance your Postgres performance. Remember that each database is unique, so always consider the specific context and use case of your queries.

## Resources

- [PostgreSQL Index Documentation](https://www.postgresql.org/docs/current/indexes.html)
- [PostgreSQL Index Types](https://www.postgresql.org/docs/current/indexes-types.html)
- [EXPLAIN Command Documentation](https://www.postgresql.org/docs/current/sql-explain.html)
- [Index Advisor Extension](https://supabase.com/docs/guides/database/extensions/index_advisor)
