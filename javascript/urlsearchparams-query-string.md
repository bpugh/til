---
date: 2024-11-07
---

# Use `URLSearchParams()` to build a query string

Today I learned that javascript has a handy built-in function called `URLSearchParams()` that you can use to build a url query string from an object.

```js
const petfinderData = {
  key: "12345",
  shelterID: "abc00",
  count: 20,
  animals: ["dogs", "cats"],
};
const query = new URLSearchParams(petfinderData);

// returns "key=12345&shelterID=abc00&count=20&animals=dogs%2Ccats"
const queryString = query.toString();
```

Read more: https://gomakethings.com/how-to-build-a-query-string-from-an-object-of-data-with-vanilla-js/

You'll want to be careful with complex object list arrays since it serializes to a form like `animals=dogs,cats`, which not be the format the server expects.

Asp.net model-binding for instance, by default expects a format like `animals=dogs&animals=cats` (and some other [variations](https://learn.microsoft.com/en-us/aspnet/core/mvc/models/model-binding?view=aspnetcore-8.0#collections)).
