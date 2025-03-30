# Working With Arrays

Postgres supports flexible [array types](https://www.postgresql.org/docs/12/arrays.html). These arrays are also supported in the Supabase Dashboard and in the JavaScript API.

## Create a Table with an Array Column

Create a test table with a text array (an array of strings):

### Using the Dashboard

1. Go to the [Table editor](https://supabase.com/dashboard/project/_/editor) page in the Dashboard.
2. Click **New Table** and create a table with the name `arraytest`.
3. Click **Save**.
4. Click **New Column** and create a column with the name `textarray`, type `text`, and select **Define as array**.
5. Click **Save**.

## Insert a Record with an Array Value

### Using the Dashboard

1. Go to the [Table editor](https://supabase.com/dashboard/project/_/editor) page in the Dashboard.
2. Select the `arraytest` table.
3. Click **Insert row** and add `["Harry", "Larry", "Moe"]`.
4. Click **Save.**

## View the Results

### Using the Dashboard

1. Go to the [Table editor](https://supabase.com/dashboard/project/_/editor) page in the Dashboard.
2. Select the `arraytest` table.

You should see:

```
| id  | textarray                |
| --- | ------------------------ |
| 1   | ["Harry","Larry","Moe"] |
```

## Query Array Data

Postgres uses 1-based indexing (e.g., `textarray[1]` is the first item in the array).

### Using SQL

To select the first item from the array and get the total length of the array:

```sql
SELECT textarray[1], array_length(textarray, 1) FROM arraytest;
```

returns:

```
| textarray | array_length |
| --------- | ------------ |
| Harry     | 3            |
```

## Resources

- [Supabase JS Client](https://github.com/supabase/supabase-js)
- [Supabase - Get started for free](https://supabase.com/)
- [Postgres Arrays](https://www.postgresql.org/docs/15/arrays.html)
