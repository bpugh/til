---
date: 2023-10-02
---

# Use the `valueAsNumber` property of html number inputs

Today I learned about the `valueAsNumber` property of html number inputs.

So instead of having to parse the value like: `const num = parseFloat(e.target.value)`

You can do: `const num = e.target.valueAsNumber`

For example in react:

```jsx
return (
    <input
      type="number"
      value={number}
      onChange={(e) => {
        // ✅
        const num = e.target.valueAsNumber
        setNumber(num)
      }}
    />
  )
```

[Work With Number and Date Inputs in JavaScript](https://www.builder.io/blog/numbers-and-dates)