---
date: 2024-07-12
---

# :has selector

Today I learned about the new `:has()` selector in CSS.

It's also referred to as the "parent" selector and that's probably the most straightforward use case but [this post](https://bejamas.io/blog/learn-css-has-selector-by-examples-top-use-cases/) shows several cool use cases.

I used it today when I needed to apply a style to a shared root element but only on a specific page, but all of the styles are bundled into a single CSS file that's loaded on every page:

```css
#app-root:has(.signin-root) {
  height: 100%;
}
```


