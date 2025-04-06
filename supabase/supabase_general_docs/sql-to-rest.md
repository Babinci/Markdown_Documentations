# SQL to REST API Translator

Translate SQL queries to HTTP requests and Supabase client code

## Overview

Sometimes it's challenging to translate SQL queries to the equivalent [PostgREST](https://postgrest.org/) request or Supabase client code. Use this tool to help with this translation.

PostgREST supports a subset of SQL, so not all SQL queries will translate.

## Example Translation

**Example SQL:**
```sql
select title, description from books 
where description ilike '%cheese%' 
order by title desc
limit 5 offset 10
```

**Translated to cURL:**
```bash
curl -G http://localhost:54321/rest/v1/books \
  -d "select=title,description" \
  -d "description=ilike.*cheese*" \
  -d "order=title.desc" \
  -d "limit=5" \
  -d "offset=10"
```

**Translated to Supabase JavaScript client:**
```javascript
const { data, error } = await supabase
  .from('books')
  .select('title, description')
  .ilike('description', '%cheese%')
  .order('title', { ascending: false })
  .range(10, 14)
```

## FAQs

**What is `curl`?**  
cURL is a command-line tool for transferring data using various protocols. It's commonly used to make HTTP requests to REST APIs.

**What do `-G` and `-d` do?**  
The `-G` flag tells curl to use a GET request and append all data specified with `-d` parameters as query parameters. Each `-d` flag adds a new query parameter to the URL.

**Why is `%` getting converted to `*`?**  
In URL encoding, the `%` character has special meaning, so PostgREST uses `*` in place of `%` in the URL parameters. The `*` is converted back to `%` when processed by PostgREST.
