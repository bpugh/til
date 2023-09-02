---
date: 2023-09-01
---

# Null values in javascript interpolated strings

Today I learned about a key difference between how javascript handles null values in interpolated strings compared to a language like C#

In C#:
``` csharp
var param1 = null;

var queryString = $"param1={param1}"; // => param1=
```

In Javascript
``` javascript
var param1 = null;

var queryString = `param1=${param1}`; // => param1=null
```

the latter is probably not what you want since your api will likely set param1 to a string value of "null".
