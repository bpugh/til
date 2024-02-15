---
date: 2024-02-15
---

# Logical Properties

I've recently been learning about the new [logical properties](https://web.dev/learn/css/logical-properties) in CSS.

Essentially if we're developing applications for a global audience, instead of thinking in terms of right/left or top/bottom, we should start thinking in terms of "inline" and "block".

These let us specify our styling and layouts in relative logical values instead of physical ones so they can adapt appropriately for right-to-left or vertical languages.

For example, `margin-left: 20px` would now be `margin-inline-start: 20px`.

These new properties are pretty well supported in browsers so I think it's probably a good practice to try to default to using them when you can even if you don't have any localization concerns.
For one, it doesn't hurt to use them and you're likely to start seeing them more and more in examples and documentation so you'll want to get used to them.

Plus you can use them as a convenient shorthand in some cases — for example, you can replace `margin-left: auto; margin-right: auto;` with just `margin-inline: auto;`.

The [CSS-Tricks article](https://css-tricks.com/css-logical-properties-and-values/) has a lot of good examples.
