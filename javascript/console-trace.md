---
date: 2024-10-10
---

# Console.trace()

#til about `console.trace()` when I needed to find out where a global function was being overridden:

```js
Object.defineProperty(window, 'setErrorMessage', {
    set(value) {
        console.trace('Global variable set:', value);
    }
});
```
This little snippet outputs a stack trace anywhere code was trying to define this global function and let me right to the culprit.

[See more about .trace()](https://developer.mozilla.org/en-US/docs/Web/API/console/trace_static)
