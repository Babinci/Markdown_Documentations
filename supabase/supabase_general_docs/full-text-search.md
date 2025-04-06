# Full Text Search in PostgreSQL

Full Text Search (FTS) allows you to efficiently search text data in your PostgreSQL database. Unlike simple text matching with `LIKE` or regular expressions, FTS understands language concepts such as stemming, ranking, and stop words to provide more relevant search results.

## Preparation

For this guide, we'll use the following example data:

| id | title | author | description |
| --- | --- | --- | --- |
| 1 | The Poky Little Puppy | Janette Sebring Lowrey | Puppy is slower than other, bigger animals. |
| 2 | The Tale of Peter Rabbit | Beatrix Potter | Rabbit eats some vegetables. |
| 3 | Tootle | Gertrude Crampton | Little toy train has big dreams. |
| 4 | Green Eggs and Ham | Dr. Seuss | Sam has changing food preferences and eats unusually colored food. |
| 5 | Harry Potter and the Goblet of Fire | J.K. Rowling | Fourth year of school starts, big drama ensues. |

## Core FTS Functions

### `to_tsvector()`

This function converts your text data into searchable tokens. `to_tsvector()` stands for "to text search vector." 

```sql
SELECT to_tsvector('green eggs and ham');
-- Returns 'egg':2 'green':1 'ham':4
```

Notice that "and" is removed (it's a stop word) and "eggs" becomes "egg" through stemming.

### `to_tsquery()`

This function converts a search query into tokens to match against. `to_tsquery()` stands for "to text search query."

```sql
SELECT to_tsquery('eggs & ham');
-- Returns 'egg' & 'ham'
```

### Match Operator: `@@`

The `@@` operator checks if a `to_tsvector` result matches a `to_tsquery` result:

```sql
SELECT to_tsvector('green eggs and ham') @@ to_tsquery('eggs & ham');
-- Returns true
```

## Basic Full Text Queries

### Search a Single Column

To find all books where the description contains the word "big":

```sql
SELECT *
FROM books
WHERE to_tsvector(description) @@ to_tsquery('big');
```

### Search Multiple Columns

To search across multiple columns, concatenate them within the `to_tsvector` function:

```sql
SELECT *
FROM books
WHERE to_tsvector(description || ' ' || title) @@ to_tsquery('little');
```

> **Important**: When concatenating columns, include a space to ensure proper tokenization.

### Match All Search Words

To find books where the description contains BOTH "little" AND "big", use the `&` operator:

```sql
SELECT *
FROM books
WHERE to_tsvector(description) @@ to_tsquery('little & big');
```

### Match Any Search Words

To find books where the description contains EITHER "little" OR "big", use the `|` operator:

```sql
SELECT *
FROM books
WHERE to_tsvector(description) @@ to_tsquery('little | big');
```

## Partial Search

Partial search allows you to match words that begin with a specific prefix.

### Using the Prefix Operator

The `:*` operator lets you perform prefix searches:

```sql
SELECT title 
FROM books 
WHERE to_tsvector(title) @@ to_tsquery('Lit:*');
```

This finds books with titles containing words that start with "Lit", such as "Little".

### Creating a Stored Procedure for Prefix Search

You can wrap the prefix search logic in a function for easier API access:

```sql
CREATE OR REPLACE FUNCTION search_books_by_title_prefix(prefix text)
RETURNS SETOF books AS $$
BEGIN
  RETURN QUERY
  SELECT * FROM books 
  WHERE to_tsvector('english', title) @@ to_tsquery(prefix || ':*');
END;
$$ LANGUAGE plpgsql;
```

### Handling Multiple Words in Queries

When searching for phrases, use the `+` operator to replace spaces:

```sql
SELECT * FROM search_books_by_title_prefix('Little+Puppy');
```

## Creating Search Indexes

For large datasets, creating an index significantly improves search performance.

### Using Generated Columns for Indexing

Create a dedicated column that stores the pre-computed `tsvector`:

```sql
ALTER TABLE books
ADD COLUMN fts tsvector 
GENERATED ALWAYS AS (to_tsvector('english', description || ' ' || title)) STORED;

CREATE INDEX books_fts ON books USING GIN (fts);
```

This creates a [GIN index](https://www.postgresql.org/docs/current/gin.html) (Generalized Inverted Index) which is optimized for FTS operations.

### Querying the Indexed Column

Once indexed, your queries become simpler and faster:

```sql
SELECT *
FROM books
WHERE fts @@ to_tsquery('little & big');
```

## Advanced Query Operators

### Proximity Searches

The `<->` operator finds words that appear near each other:

```sql
-- Words adjacent to each other
SELECT *
FROM books
WHERE to_tsvector(description) @@ to_tsquery('big <-> dreams');

-- Words within 2 words of each other
SELECT *
FROM books
WHERE to_tsvector(description) @@ to_tsquery('year <2> school');
```

### Negation

The `!` operator excludes words from the search:

```sql
SELECT *
FROM books
WHERE to_tsvector(description) @@ to_tsquery('big & !little');
```

This finds books with "big" but not "little" in the description.

## Language Support

By default, PostgreSQL uses English stemming rules. To specify a different language:

```sql
SELECT to_tsvector('spanish', 'Los perros y gatos');
```

## Performance Considerations

1. **Always index** your search columns for production use
2. **Use generated columns** to maintain search vectors automatically
3. **Consider query complexity** - complex queries may require more resources
4. **Monitor performance** of FTS queries in production
5. **Use language-specific configurations** for non-English content

## Resources

For more advanced usage, refer to:
- [PostgreSQL Text Search Functions and Operators](https://www.postgresql.org/docs/current/functions-textsearch.html)
- [PostgreSQL Full Text Search Introduction](https://www.postgresql.org/docs/current/textsearch-intro.html)
