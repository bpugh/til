---
date: 2024-02-08
---

# Number.isInteger()

Today I learned that the [`isNaN`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/isNaN) global function in javascript isn't very useful for validating numbers.
The main reason is that it returns `false` for an empty string since it coerces it to `0`.

To add to the confusion, [`Number.isNaN()` behaves slightly differently](https://stackoverflow.com/questions/33164725/confusion-between-isnan-and-number-isnan-in-javascript) since it just checks for the value `NaN`.

For validation, I found [`Number.isInteger()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Number/isInteger) to be the most useful.
