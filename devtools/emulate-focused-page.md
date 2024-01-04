---
date: 2023-08-28
---

# Emulate page focus

Today I learned about a devtools feature that helped me debug the styling of an element that would disappear when the input element lost focus which happens when you click over to the devtools.

If you press `ctrl+shift+p` to open the command palette in DevTools, and type "focus", you'll see a command to "Emulate a focused page" which will leave the focus on the element in the page even when you click into the DevTools.

[This post](https://levelup.gitconnected.com/different-ways-to-inspect-disappearing-elements-on-a-browser-5df42888b7cf) shows several other techniques you could potentially use but I found this option to work best for my scenario.

My favorite technique is this clever javascript snippet you can run from the console:

```js
setTimeout(function () {
  debugger;
}, 3000);
```
