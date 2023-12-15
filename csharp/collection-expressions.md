---
date: 2023-12-14
---

# Collection expressions

Today I learned that C# 12 is getting some nice javascript-like syntax with collection expressions and the `..` (spread operator):

```csharp
string[] moreFruits = ["orange", "pear"];
IEnumerable<string> fruits = ["apple", "banana", "cherry", ..moreFruits];
```

Note though that the spread operator is only 2 dots instead of 3 dots like in javascript.