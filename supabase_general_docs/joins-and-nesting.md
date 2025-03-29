# Querying Joins and Nested Tables

The data APIs automatically detect relationships between Postgres tables. Since Postgres is a relational database, this is a very common scenario.

## One-to-many joins

Let's use an example database that stores `orchestral_sections` and `instruments`:

**Orchestral sections**

| `id` | `name` |
| --- | --- |
| 1 | strings |
| 2 | woodwinds |

**Instruments**

| `id` | `name` | `section_id` |
| --- | --- | --- |
| 1 | violin | 1 |
| 2 | viola | 1 |
| 3 | flute | 2 |
| 4 | oboe | 2 |

The APIs will automatically detect relationships based on the foreign keys:

```javascript
const { data, error } = await supabase.from('orchestral_sections').select(`
  id,
  name,
  instruments ( id, name )
`)
```

### TypeScript types for joins

`supabase-js` always returns a `data` object (for success), and an `error` object (for unsuccessful requests).

These helper types provide the result types from any query, including nested types for database joins.

Given the following schema with a relation between orchestral sections and instruments:

```sql
CREATE TABLE orchestral_sections (
  "id" serial primary key,
  "name" text
);

CREATE TABLE instruments (
  "id" serial primary key,
  "name" text,
  "section_id" int references "orchestral_sections"
);
```

We can get the nested `SectionsWithInstruments` type like this:

```typescript
import { QueryResult, QueryData, QueryError } from '@supabase/supabase-js'

const sectionsWithInstrumentsQuery = supabase.from('orchestral_sections').select(`
  id,
  name,
  instruments (
    id,
    name
  )
`)

type SectionsWithInstruments = QueryData<typeof sectionsWithInstrumentsQuery>

const { data, error } = await sectionsWithInstrumentsQuery
if (error) throw error

const sectionsWithInstruments: SectionsWithInstruments = data
```

## Many-to-many joins

The data APIs will detect many-to-many joins. For example, if you have a database which stored teams of users (where each user could belong to many teams):

```sql
CREATE TABLE users (
  "id" serial primary key,
  "name" text
);

CREATE TABLE teams (
  "id" serial primary key,
  "team_name" text
);

CREATE TABLE members (
  "user_id" int references users,
  "team_id" int references teams,
  primary key (user_id, team_id)
);
```

In these cases you don't need to explicitly define the joining table (members). If we wanted to fetch all the teams and the members in each team:

```javascript
const { data, error } = await supabase.from('teams').select(`
  id,
  team_name,
  users ( id, name )
`)
```

## Specifying the `ON` clause for joins with multiple foreign keys

For example, if you have a project that tracks when employees check in and out of work shifts:

```sql
-- Employees
CREATE TABLE users (
  "id" serial primary key,
  "name" text
);

-- Badge scans
CREATE TABLE scans (
  "id" serial primary key,
  "user_id" int references users,
  "badge_scan_time" timestamp
);

-- Work shifts
CREATE TABLE shifts (
  "id" serial primary key,
  "user_id" int references users,
  "scan_id_start" int references scans, -- clocking in
  "scan_id_end" int references scans, -- clocking out
  "attendance_status" text
);
```

In this case, you need to explicitly define the join because the joining column on `shifts` is ambiguous as they are both referencing the `scans` table.

To fetch all the `shifts` with `scan_id_start` and `scan_id_end` related to a specific `scan`, use the following syntax:

```javascript
const { data, error } = await supabase.from('shifts').select(
  `
    *,
    start_scan:scans!scan_id_start (
      id,
      user_id,
      badge_scan_time
    ),
   end_scan:scans!scan_id_end (
     id,
     user_id,
     badge_scan_time
    )
  `
)
```
