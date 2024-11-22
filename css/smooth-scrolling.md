---
date: 2024-01-08
---

# Smooth scrolling

Today I learned that you can now implement smooth scrolling purely with CSS in modern browsers.

By adding the following CSS:

```css
/* Smooth scrolling IF user doesn't have a preference due to motion sensitivities */
@media screen and (prefers-reduced-motion: no-preference) {
  html {
    scroll-behavior: smooth;
  }
}
```
the browser will scroll smoothly whenever scrolling is triggered either by Javascript (with something like `document.documentElement.scrollTop = 0`) or by linking to elements with an internal anchor link.
It's considered best practice to use the `prefers-reduced-motion` media query to only enable things like animations to be mindful of users with motion sensitivities.
In my testing, however, the browser won't ever smooth scroll if the user has `prefers-reduced-motion` enabled.

Another way of accomplishing this is with the [`scrollTo`](https://developer.mozilla.org/en-US/docs/Web/API/Window/scrollTo) function in javascript:

`window.scrollTo({top:0, behavior: 'smooth'})`

or with the [scrollIntoView](https://developer.mozilla.org/en-US/docs/Web/API/Element/scrollIntoView) function.

I also discovered that `prefers-reduced-motion` is controlled at the system level — in Windows it's determined by the "Show animations in Windows" setting which is automatically disabled when connecting to Windows via Remote Desktop.

https://developer.mozilla.org/en-US/docs/Web/CSS/scroll-behavior
