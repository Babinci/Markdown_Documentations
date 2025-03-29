# High Latency with Supabase Client

This guide helps you understand and troubleshoot cases where querying a table using the Supabase client is much slower than querying against the Postgres database directly.

## Issue Description

When using the Supabase client to query your database, you may notice a significant latency difference compared to direct PostgreSQL queries. This overhead can be particularly noticeable for smaller tables or queries returning just one row.

## Reproducing the Issue

You can test the latency difference with the following steps:

1. First, create a test table with some sample data:

```sql
-- Create table
CREATE TABLE your_table_name (
    id UUID PRIMARY KEY,
    column1 TEXT,
    column2 INT,
    column3 BOOLEAN
);

-- Insert statements
INSERT INTO your_table_name (id, column1, column2, column3) VALUES
    (uuid_generate_v4(), 'value1', 10, TRUE),
    (uuid_generate_v4(), 'value2', 20, FALSE),
    (uuid_generate_v4(), 'value3', 15, TRUE),
    -- Add more test rows as needed
    (uuid_generate_v4(), 'value20', 21, FALSE);
```

2. Run the following script to compare query times (requires Python with `psycopg` and the Supabase client):

```python
import time
from supabase import Client, create_client
import psycopg

def psycop_call():
    user="YOUR_SUPABASE_USER"
    password="YOUR_SUPABASE_PASSWORD"
    host="SUPABASE_HOST"
    port=5432
    database="postgres"
    with psycopg.connect(f"host={host} port={port} dbname={database} user={user} password={password}") as conn:
        results = []
        with conn.cursor() as cur:
            start = time.time()
            cur.execute("SELECT * FROM public.your_table_name")
            cur.fetchall()
            for record in cur:
                results.append(record)
            stop = time.time()
            return (stop - start)

def supabase_call():
    supabase: Client = create_client("SUPABASE_URL", "SUPBASE_SERVICE_ROLE_KEY")
    start = time.time()
    result = supabase.table("your_table_name").select("*").execute()
    stop = time.time()
    return (stop - start)

if __name__ == "__main__":
    ref = psycop_call()
    sup = supabase_call()
    print(f"postgres: {ref}, supabase: {sup}, ratio: {sup/ref}")
```

## Expected Behavior

The overhead from the Supabase client (which uses PostgREST) should not be significantly higher than direct PostgreSQL queries. A small overhead of a few milliseconds is expected, but large differences (such as 60-70ms or more) could indicate a potential issue.

## Understanding the Difference

It's important to note that when running queries in the SQL Editor in the Supabase Dashboard, the reported execution time reflects only the PostgreSQL query execution time, not the additional latency introduced by the API layer. This can sometimes be misleading when comparing to client library performance.

## Possible Solutions

1. **Optimize query patterns:**
   - Use targeted queries that select only necessary columns
   - Implement pagination for large result sets
   - Add appropriate indexes for your query patterns

2. **Consider using database functions:**
   - For complex operations, consider creating PostgreSQL functions that can be called via a single RPC call

3. **Direct PostgreSQL connection:**
   - For performance-critical operations, consider using a direct PostgreSQL connection instead of the REST API
   - Note that this requires proper security setup, as direct connections bypass Row Level Security

4. **Use batch operations:**
   - When possible, batch multiple operations into a single request to reduce the number of API calls
