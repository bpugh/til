---
date: 2023-11-29
---

# Flow spacing and the lobotomized owl

This is another #til by proxy. A teammate asked about a CSS selector I used which has come to be referred to as the ["lobotomized owl"](https://alistapart.com/article/axiomatic-css-and-lobotomized-owls/) (`* + *`):

``` css
.flow > * + * {
  margin-top: var(--flow-space, 1em);
}
```

What this does is select every child element of the `.flow` class except the first one.

You can also use newer CSS selectors to do the same thing in a way that might be more obvious:

```css
.flow > *:where(:not(:first-child)) {
  margin-top: var(--flow-space, 1em);
}
```

The above snippet is probably my favorite CSS utility called [flow spacing](https://24ways.org/2018/managing-flow-and-rhythm-with-css-custom-properties/).

It's a nice way to easily add consistent spacing between elements in your project and because css variables cascade, it's easy to override for specific contexts within different classes:

```css
.flow--space-compact {
  --flow-space: .75em;
}
```

or with inline styles: `<footer class="flow" style="--flow-space: 2em"></footer>`.

I'm in the camp that parent components should be responsible for spacing out their child components and this utility makes that easier to do with consistency.


