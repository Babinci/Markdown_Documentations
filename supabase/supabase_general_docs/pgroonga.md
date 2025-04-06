# PGroonga: Multilingual Full Text Search

`PGroonga` is a PostgreSQL extension adding a full text search indexing method based on [Groonga](https://groonga.org/). While native PostgreSQL supports full text indexing, it is limited to alphabet and digit-based languages. `PGroonga` offers a wider range of character support, making it viable for a superset of languages supported by PostgreSQL including Japanese, Chinese, and more.

## Enable the extension

### Using the Dashboard

1. Go to the Database page in the Dashboard
2. Click on **Extensions** in the sidebar
3. Search for `pgroonga` and enable the extension

### Using SQL

```sql
create extension pgroonga;
```

## Creating a full text search index

Given a table with a `text` column:

```sql
create table memos (
  id serial primary key,
  content text
);
```

We can index the column for full text search with a `pgroonga` index:

```sql
create index ix_memos_content ON memos USING pgroonga(content);
```

To test the full text index, we'll add some data:

```sql
insert into memos(content) values
  ('PostgreSQL is a relational database management system.'),
  ('Groonga is a fast full text search engine that supports all languages.'),
  ('PGroonga is a PostgreSQL extension that uses Groonga as index.'),
  ('There is groonga command.');
```

The PostgreSQL query planner is smart enough to know that, for extremely small tables, it's faster to scan the whole table rather than loading an index. To force the index to be used, we can disable sequential scans:

```sql
-- For testing only. Don't do this in production
set enable_seqscan = off;
```

Now if we run an explain plan on a query filtering on `memos.content`:

```sql
explain select * from memos where content like '%engine%';
```

The `pgroonga` index is used to retrieve the result set:

```
                              QUERY PLAN
-----------------------------------------------------------------------------
Index Scan using ix_memos_content on memos  (cost=0.00..1.11 rows=1 width=36)
  Index Cond: (content ~~ '%engine%'::text)
(2 rows)
```

And the query result would be:

```
| id  | content                                                                  |
| --- | ------------------------------------------------------------------------ |
| 2   | 'Groonga is a fast full text search engine that supports all languages.' |
```

## Full text search

The `&@~` operator performs full text search. It returns any matching results. Unlike the `LIKE` operator, `pgroonga` can search any text that contains the keyword case-insensitively.

Take the following example:

```sql
select * from memos where content &@~ 'groonga';
```

And the result:

```
id | content
----+------------------------------------------------------------------------
2 | Groonga is a fast full text search engine that supports all languages.
3 | PGroonga is a PostgreSQL extension that uses Groonga as index.
4 | There is groonga command.
(3 rows)
```

### Match all search words

To find all memos where content contains BOTH of the words `postgres` and `pgroonga`, we can use spaces to separate each word:

```sql
select * from memos where content &@~ 'postgres pgroonga';
```

And the result:

```
id | content
----+----------------------------------------------------------------
3 | PGroonga is a PostgreSQL extension that uses Groonga as index.
(1 row)
```

### Match any search words

To find all memos where content contains ANY of the words `postgres` or `pgroonga`, use the upper case `OR`:

```sql
select * from memos where content &@~ 'postgres OR pgroonga';
```

And the result:

```
id | content
----+----------------------------------------------------------------
1 | PostgreSQL is a relational database management system.
3 | PGroonga is a PostgreSQL extension that uses Groonga as index.
(2 rows)
```

### Search that matches words with negation

To find all memos where content contains the word `postgres` but not `pgroonga`, use the `-` symbol:

```sql
select * from memos where content &@~ 'postgres -pgroonga';
```

And the result:

```
id | content
----+--------------------------------------------------------
1 | PostgreSQL is a relational database management system.
(1 row)
```

## Resources

- Official [PGroonga documentation](https://pgroonga.github.io/tutorial/)
