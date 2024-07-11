---
date: 2024-07-10
---

# Use media queries in javascript with the `matchMedia()` method

Today I learned that the `matchMedia()` javascript method lets you match against media queries and respond accordingly with javascript.

That could look something like this:

```js
const mediaQuery = window.matchMedia('(min-width: 768px)')
// Check if the media query is true
if (mediaQuery.matches) {
  // Then trigger an alert
  alert('Media Query Matched!')
}
```
You can also add an event listener to the `mediaQuery` which you'll want to do to respond to the user changing the size of the window — see [this post](https://css-tricks.com/working-with-javascript-media-queries/) for details on how to do that.

Ideally, I try to keep media queries in CSS but this can come in handy for example if you want to change the way a tooltip behaves on smaller screens.

