# Converting SQL to JavaScript API

Many common SQL queries can be written using the JavaScript API, provided by the SDK to wrap Data API calls. Below are a few examples of conversions between SQL and JavaScript patterns.

## Select Statement with Basic Clauses

Select a set of columns from a single table with where, order by, and limit clauses.

```sql
select first_name, last_name, team_id, age
from players
where age between 20 and 24 and team_id != 'STL'
order by last_name, first_name desc
limit 20;
```

```javascript
const { data, error } = await supabase
  .from('players')
  .select('first_name,last_name,team_id,age')
  .gte('age', 20)
  .lte('age', 24)
  .not('team_id', 'eq', 'STL')
  .order('last_name', { ascending: true }) // or just .order('last_name')
  .order('first_name', { ascending: false })
  .limit(20)
```

## Select Statement with Complex Boolean Logic Clause

Select all columns from a single table with a complex where clause: OR AND OR

```sql
select *
from players
where ((team_id = 'CHN' or team_id is null) and (age > 35 or age is null));
```

```javascript
const { data, error } = await supabase
  .from('players')
  .select() // or .select('*')
  .or('team_id.eq.CHN,team_id.is.null')
  .or('age.gt.35,age.is.null') // additional filters imply "AND"
```

Select all columns from a single table with a complex where clause: AND OR AND

```sql
select *
from players
where ((team_id = 'CHN' and age > 35) or (team_id != 'CHN' and age is not null));
```

```javascript
const { data, error } = await supabase
  .from('players')
  .select() // or .select('*')
  .or('and(team_id.eq.CHN,age.gt.35),and(team_id.neq.CHN,.not.age.is.null)')
```

## Resources

- [Supabase - Get started for free](https://supabase.com/)
- [PostgREST Operators](https://postgrest.org/en/stable/api.html#operators)
- [Supabase API: JavaScript select](https://supabase.com/docs/reference/javascript/select)
- [Supabase API: JavaScript modifiers](https://supabase.com/docs/reference/javascript/using-modifiers)
- [Supabase API: JavaScript filters](https://supabase.com/docs/reference/javascript/using-filters)
