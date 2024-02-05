---
date: 2023-07-06
---

# Hide a table in sql server management studio

Apparently in sql server you can mark any table as a system table using `EXEC sys.sp_MS_marksystemobject` and then Management studio will hide it automatically.

I ran into this because the docs say that Entity Framework 6 stores its code-first migration snapshots in a table called `__MigrationHistory` but I couldn't find it because it's _hidden_ since it's marked as a system table.
