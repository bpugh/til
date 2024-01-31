---
date: 2024-01-31
---

# Javascript Array `with()` method

Today I learned that there's a new javascript array method that returns a _new_ array with the element at the given index replaced with the given value.

Convenient for manipulating array values without mutating the original array.

```js
const arr = [1, 2, 3, 4, 5];
console.log(arr.with(2, 6)); // [1, 2, 6, 4, 5]
console.log(arr); // [1, 2, 3, 4, 5]
```