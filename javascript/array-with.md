---
date: 2023-08-11
---

# Javascript Array.prototype.with()

I just discovered the `with()` method which takes an index value and a value to insert at that index and returns a new array with the value inserted at the index.

``` javascript
const arr = [1, 2, 3, 4, 5];
const newArr = arr.with(2, 'a');
console.log(newArr); // [1, 2, 'a', 3, 4, 5]
```

You could definitely do this before with something like `arr[2] = 'a'` but that would modify the original array

The `with()` method became widely supported in 2021.

Read more about the `with()` method and alternatives in [Stefan Judis' post](https://www.stefanjudis.com/snippets/copy-array-and-replace-one-element-at-index-javascript/).
