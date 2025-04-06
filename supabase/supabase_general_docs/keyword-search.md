# Keyword Search

Learn how to implement and use keyword-based search functionality with PostgreSQL in Supabase.

## Overview

Keyword search involves locating documents or records that contain specific words or phrases, primarily based on the exact match between the search terms and the text within the data. It differs from [semantic search](semantic-search.md), which interprets the meaning behind the query to provide results that are contextually related, even if the exact words aren't present in the text.

In PostgreSQL, keyword search is implemented using [full-text search](full-text-search.md). It supports indexing and text analysis for data retrieval, focusing on records that match the search criteria. PostgreSQL's full-text search extends beyond simple keyword matching to address linguistic nuances, making it effective for applications that require precise text queries.

## When and Why to Use Keyword Search

Keyword search is particularly useful in scenarios where precision and specificity matter. It's more effective than semantic search when users are looking for information using exact terminology or specific identifiers. It ensures that results directly contain those terms, reducing the chance of retrieving irrelevant information.

Use keyword search for:

- **Exact Matches**: When users need documents that contain specific terms
- **Structured Data Search**: When searching within well-defined fields like product names, categories, or tags
- **Technical Documentation**: Where specific terminology, error codes, or command names are used
- **Compliance and Legal Search**: Where exact phrases or terms have legal significance
- **Resource-Constrained Systems**: When you need efficient search without the computational overhead of vector embeddings

For example, in technical or academic research databases, researchers often search for specific studies, compounds, or concepts identified by certain terms or codes. Searching for a specific chemical compound using its exact molecular formula or a unique identifier will yield more focused and relevant results compared to a semantic search.

## Using PostgreSQL Full-Text Search

PostgreSQL's full-text search capabilities include:

1. **Text Search Configurations**: Language-specific analysis of words
2. **Text Search Types**: `tsvector` (document) and `tsquery` (query)
3. **Text Search Operators**: Boolean operations like `&` (AND), `|` (OR), and `!` (NOT)
4. **Text Search Functions**: Functions for creating and manipulating search objects
5. **Text Search Indexing**: GIN and GiST indexes for efficient queries

### Basic Example

```sql
-- Create a table with a text column
CREATE TABLE articles (
  id SERIAL PRIMARY KEY,
  title TEXT,
  body TEXT
);

-- Insert some sample data
INSERT INTO articles (title, body) VALUES 
  ('PostgreSQL Tutorial', 'PostgreSQL is a powerful, open source object-relational database system'),
  ('Full Text Search', 'Full text search provides a means of identifying natural-language documents'),
  ('Supabase Features', 'Supabase provides authentication, real-time subscriptions, and storage');

-- Create a function to search articles
CREATE FUNCTION search_articles(search_term TEXT) 
RETURNS TABLE (id INT, title TEXT, body TEXT, rank REAL) AS $$
  SELECT
    id,
    title,
    body,
    ts_rank(
      setweight(to_tsvector('english', title), 'A') || 
      setweight(to_tsvector('english', body), 'B'),
      to_tsquery('english', search_term)
    ) AS rank
  FROM articles
  WHERE 
    to_tsvector('english', title) || to_tsvector('english', body) @@ to_tsquery('english', search_term)
  ORDER BY rank DESC;
$$ LANGUAGE SQL;

-- Search for articles containing 'postgresql'
SELECT * FROM search_articles('postgresql');
```

### Adding Indexes for Performance

For better performance with large datasets, add GIN indexes:

```sql
-- Add GIN indexes for faster full-text search
CREATE INDEX articles_title_idx ON articles USING GIN (to_tsvector('english', title));
CREATE INDEX articles_body_idx ON articles USING GIN (to_tsvector('english', body));
```

## Combining with Other Search Methods

It's possible to combine keyword search with semantic search to get the best of both worlds. See [Hybrid Search](hybrid-search.md) for more details on implementing a combined approach.

## Resources

- [Full Text Search in PostgreSQL](full-text-search.md) - Comprehensive guide to implementing full-text search
- [Semantic Search](semantic-search.md) - Understanding meaning-based search with vector embeddings
- [Hybrid Search](hybrid-search.md) - Combining keyword and semantic search techniques
