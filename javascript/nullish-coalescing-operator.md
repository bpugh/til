---
date: 2024-06-03
---

# Nullish Coalescing Operator

Today I learned that javascript gained a [nullish coalescing operator](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Nullish_coalescing) (`??`) in ECMAScript 2020.

```js
const result = potentialEmpty ?? fallbackValue;
```

It return the right operand if the left operand is null or undefined so for me this is a convenient alternative to using the OR (`||`) operator if I don't want the fallbackValue on falsy values like `0` or an empty string.
