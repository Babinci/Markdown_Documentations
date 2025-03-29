# Selecting the First Row for Each Group in PostgreSQL

This guide demonstrates how to select the first row for each group in PostgreSQL using the `DISTINCT ON` clause, which is a powerful feature for retrieving unique records based on specific criteria.

## Problem

A common database challenge is finding the first (or maximum/minimum) row for each group of records. For example, you might want to find:
- The highest score for each player
- The most recent order for each customer
- The maximum points for each team

## Sample Data

Consider a table called `seasons` with the following data:

| id | team      | points |
|----|-----------|--------|
| 1  | Liverpool | 82     |
| 2  | Liverpool | 84     |
| 3  | Brighton  | 34     |
| 4  | Brighton  | 28     |
| 5  | Liverpool | 79     |

## Finding the Maximum Points per Team

To find the records with the maximum number of points for each team:

```sql
SELECT DISTINCT ON (team) 
  id,
  team,
  points
FROM 
  seasons
ORDER BY 
  team,
  points DESC;
```

### Expected Result

| id | team      | points |
|----|-----------|--------|
| 3  | Brighton  | 34     |
| 2  | Liverpool | 84     |

## How It Works

The `DISTINCT ON` query works in the following way:

1. **Grouping**: `DISTINCT ON (team)` groups the rows by the `team` column
2. **Ordering**: `ORDER BY team, points DESC` first sorts by team (to group them), then by points in descending order
3. **Selection**: For each distinct value of `team`, it selects the first row according to the order specified

The key is that **ordering matters**. The first row encountered for each group will be selected, so the order must be defined to put the desired row (highest points, most recent date, etc.) first.

## Additional Examples

### Finding the Most Recent Order for Each Customer

```sql
SELECT DISTINCT ON (customer_id)
  order_id,
  customer_id,
  order_date,
  amount
FROM
  orders
ORDER BY
  customer_id,
  order_date DESC;
```

### Finding the Lowest Price for Each Product

```sql
SELECT DISTINCT ON (product_id)
  price_id,
  product_id,
  price,
  effective_date
FROM
  product_prices
ORDER BY
  product_id,
  price ASC;
```

## Alternative Approaches

While `DISTINCT ON` is PostgreSQL specific, alternative approaches include:

### Using Window Functions

```sql
SELECT id, team, points
FROM (
  SELECT 
    id, 
    team, 
    points,
    ROW_NUMBER() OVER (PARTITION BY team ORDER BY points DESC) as rn
  FROM 
    seasons
) t
WHERE rn = 1;
```

### Using a Common Table Expression (CTE)

```sql
WITH ranked_seasons AS (
  SELECT 
    id, 
    team, 
    points,
    ROW_NUMBER() OVER (PARTITION BY team ORDER BY points DESC) as rn
  FROM 
    seasons
)
SELECT id, team, points
FROM ranked_seasons
WHERE rn = 1;
```

## Performance Considerations

`DISTINCT ON` is generally efficient in PostgreSQL and often offers better performance than alternatives for this specific use case. However, for optimal performance, consider creating an index on the columns used in the `DISTINCT ON` and `ORDER BY` clauses.
