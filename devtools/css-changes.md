---
date: 2023-08-15
---

# Find all CSS changes in Chrome DevTools

Today I learned about the [Changes tab](https://developer.chrome.com/docs/devtools/changes/) in Chrome devtools.

When you're tweaking CSS styles in Chrome DevTools, you can see all the changes you've made by clicking the "Changes" tab in the bottom "drawer" in DevTools.
It's especially nice because you can then copy the changes to your clipboard and paste them into your actual source file.
You can open it from the command palette (`ctrl+shift+p`) and typing "show changes".

One caveat I've noticed is that it doesn't show styles you've added directly to an element as an inline style.
