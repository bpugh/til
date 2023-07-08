---
date: 2023-07-04
---

# Use a table variable to hold a list of values

You can store a "list" of values in sql with a `table` variable.

```sql
DECLARE @listOfIDs TABLE(id INT);
INSERT INTO @listOfIDs
SELECT id
FROM Transactions
WHERE USER='bob';
```
