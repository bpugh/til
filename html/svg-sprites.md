---
date: 2023-09-28
---

# SVG sprites

Today I learned about the `<use>` element and how you can use it to create [_SVG_ sprites](https://benadam.me/thoughts/react-svg-sprites/).
It turns out that my preferred way of working with svgs in react by embedding them in the components, [is not great for performance](https://kurtextrem.de/posts/svg-in-js) or bundle size.
But as [Ben Adam's post shows](https://benadam.me/thoughts/react-svg-sprites/), it looks like inline svgs using sprites gives you the best performance to development experience tradoff.
