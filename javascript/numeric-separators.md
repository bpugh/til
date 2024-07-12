---
date: 2024-07-02
---

# Numeric separators

Today I learned about [numeric separators](https://v8.dev/features/numeric-separators) in javascript.
They are a small bit of syntactic sugar to make large numeric literals easier to read by letting you insert underscores anywhere in the number.

For example, if you need to specify 10mb in byes, instead of `10485760`, you can write it as:

```js
const maxUploadSize = 10_485_760;
```

They were added in ECMAScript 2021 and in C# 7.