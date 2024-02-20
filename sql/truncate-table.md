---
date: 2024-02-20
---

# Truncate table

Today I learned that there is a `truncate table` SQL command that deletes all data from a database table like `Delete from` but is faster and uses fewer system and transaction log resources.

It's supported in most database engines but there are likely caveats to keep in mind.

For instance, with SQL Server:

* It will reseed identity columns
* You can't truncate tables that referenced in constraints
* and it requires ALTER table privileges

For clearing out data in lower environments though, I've found it useful.
