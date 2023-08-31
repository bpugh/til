---
date: 2023-08-30
---

# Object.fromEntries

#til about [Object.fromEntries()](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Object/fromEntries) in javascript which essentially lets you convert a list of key/value pairs into an object (this is the same as the lodash function `fromPairs`).

This came in handy when I needed to convert a list of entities into a lookup object like:

```javascript
Object.fromEntries(
  users.map((user) => {
    return [user.id, user.isSelected];
  })
); // => { '1': true, '2': false, '3': false }
```

