---
date: 2023-11-01
---

# `every()` returns true for an empty array

Today I learned that the javascript array method `.every()` will always return true for an empty array.

``` js
[].every((x) => x > 1);         // true
[].every(() => true);           // true
[].every(() => false);          // true
```

For me at least, this was a bit surprising and I realized I'd been thinking about this function works incorrectly.
Your first thought might be that this is another one of javascript's quirks, but this is actually how most languages implement similar functions including Rust, Python, and C#:

``` csharp
result = new List<int>().All(x => x > 0);   // true
result = new List<int>().All(x => false);   // true
```

Apparently this is because of Math. Specifically, it's meant to behave the same as the "for all" quantifier in mathematics.

[Nicholas Zakas has a good article](https://humanwhocodes.com/blog/2023/09/javascript-wtf-why-does-every-return-true-for-empty-array/#user-content-fn-10) that goes into more detail and this nice tip if you also found this behavior surprising:

> Instead of reading every() as “does every item in this array match this condition?” read it as, “is there any item in this array that doesn’t match this condition?”
