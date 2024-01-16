---
date: 2024-01-15
---

# Dynamically darken or lighten a color in CSS

Today I learned that you can now easily darken or lighten a color natively in CSS with the new [color-mix](https://developer.chrome.com/docs/css-ui/css-color-mix) function.

Here's a use case I run into a lot where you have a primary brand color and you need to darken it on hover:

```css
:root {
  --brand-color-dark: color-mix(in oklab, var(--brand-color), black 30%);
  --brand-color-light: color-mix(in oklab, var(--brand-color), white 30%);
}

.button:hover {
  background-color: var(--brand-color-dark)
}
```

This works by mixing the color with some amount of black or white. I also chose the `oklab` [color space](https://developer.chrome.com/docs/css-ui/high-definition-css-color-guide#meet_the_new_web_color_spaces) since it's the most likely to produce what I'm expecting for this use case.

I've accomplished this before by using HSL color values with CSS variables and manipulating the lightness channel but this is much nicer and works even if the base color is defined as a hex value (that may or may not come from a database somewhere).

I was missing something like this from preprocessors like LESS and SASS and as of 2023 this is supported in all modern browsers.
