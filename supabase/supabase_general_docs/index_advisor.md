# Index Advisor: Query Optimization

[Index Advisor](https://github.com/supabase/index_advisor) is a Postgres extension for recommending indexes to improve query performance.

Features:

- Supports generic parameters e.g. `$1`, `$2`
- Supports materialized views
- Identifies tables/columns obfuscated by views
- Skips duplicate indexes

`index_advisor` is accessible directly through Supabase Studio by navigating to the [Query Performance Report](https://supabase.com/dashboard/project/_/advisors/query-performance) and selecting a query and then the "indexes" tab.

![Supabase Studio index_advisor integration.](https://supabase.com/docs/img/index_advisor_studio.png)

Alternatively, you can use index_advisor directly via SQL.

For example:

```sql
SELECT *
FROM index_advisor('SELECT book.id FROM book WHERE title = $1');
```

Result:
```
 startup_cost_before | startup_cost_after | total_cost_before | total_cost_after |                  index_statements                   | errors
---------------------+--------------------+-------------------+------------------+-----------------------------------------------------+--------
 0.00                | 1.17               | 25.88             | 6.40             | {"CREATE INDEX ON public.book USING btree (title)"},| {}
(1 row)
```

## Installation

To get started, enable index_advisor by running:

```sql
CREATE EXTENSION index_advisor;
```

## API

Index advisor exposes a single function `index_advisor(query text)` that accepts a query and searches for a set of SQL DDL `CREATE INDEX` statements that improve the query's execution time.

The function's signature is:

```sql
index_advisor(query text)
RETURNS TABLE (
    startup_cost_before jsonb,
    startup_cost_after jsonb,
    total_cost_before jsonb,
    total_cost_after jsonb,
    index_statements text[],
    errors text[]
)
```

## Usage

As a minimal example, the `index_advisor` function can be given a single table query with a filter on an unindexed column.

```sql
CREATE EXTENSION IF NOT EXISTS index_advisor CASCADE;

CREATE TABLE book(
  id int PRIMARY KEY,
  title text NOT NULL
);

SELECT *
FROM index_advisor('SELECT book.id FROM book WHERE title = $1');
```

Result:
```
 startup_cost_before | startup_cost_after | total_cost_before | total_cost_after |                  index_statements                   | errors
---------------------+--------------------+-------------------+------------------+-----------------------------------------------------+--------
 0.00                | 1.17               | 25.88             | 6.40             | {"CREATE INDEX ON public.book USING btree (title)"},| {}
(1 row)
```

and will return a row recommending an index on the unindexed column.

More complex queries may generate additional suggested indexes:

```sql
CREATE EXTENSION IF NOT EXISTS index_advisor CASCADE;

CREATE TABLE author(
    id serial PRIMARY KEY,
    name text NOT NULL
);

CREATE TABLE publisher(
    id serial PRIMARY KEY,
    name text NOT NULL,
    corporate_address text
);

CREATE TABLE book(
    id serial PRIMARY KEY,
    author_id int NOT NULL REFERENCES author(id),
    publisher_id int NOT NULL REFERENCES publisher(id),
    title text
);

CREATE TABLE review(
    id serial PRIMARY KEY,
    book_id int REFERENCES book(id),
    body text NOT NULL
);

SELECT *
FROM index_advisor('
    SELECT
        book.id,
        book.title,
        publisher.name AS publisher_name,
        author.name AS author_name,
        review.body review_body
    FROM
        book
        JOIN publisher
            ON book.publisher_id = publisher.id
        JOIN author
            ON book.author_id = author.id
        JOIN review
            ON book.id = review.book_id
    WHERE
        author.id = $1
        AND publisher.id = $2
');
```

Result:
```
 startup_cost_before | startup_cost_after | total_cost_before | total_cost_after |                  index_statements                         | errors
---------------------+--------------------+-------------------+------------------+-----------------------------------------------------------+--------
 27.26               | 12.77              | 68.48             | 42.37            | {"CREATE INDEX ON public.book USING btree (author_id)",   | {}
                                                                                 "CREATE INDEX ON public.book USING btree (publisher_id)",
                                                                                 "CREATE INDEX ON public.review USING btree (book_id)"}
(3 rows)
```

## Limitations

- Index_advisor will only recommend single column, B-tree indexes. More complex indexes will be supported in future releases.
- When a generic argument's type is not discernible from context, an error is returned in the `errors` field. To resolve those errors, add explicit type casting to the argument. e.g. `$1::int`.

## Resources

- [`index_advisor`](https://github.com/supabase/index_advisor) repository
