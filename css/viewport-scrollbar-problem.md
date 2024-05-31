---
date: 2024-05-28
title: The viewport scroll bar problem
---

# The viewport scroll bar problem

Today I learned that the viewport units in CSS don't account for the width of visible classic scrollbars like on Windows.

This means that if you use `width: 100vw` to make an element the full width of the page and then a scrollbar appears, it will cause the element to overflow (by 17px which is apparently the width of Windows scrollbars) and create a horizontal scrollbar.

CSS media queries don't take them into account either, so if the viewport width is close (say within 17px) of a breakpoint then the appearance of a scrollbar will cause it to cross that threshold.

[This article](https://www.smashingmagazine.com/2023/12/new-css-viewport-units-not-solve-classic-scrollbar-problem/#avoiding-the-classic-scrollbar-problem) gives some potential solutions:

1. Use the new CSS container queries
2. Use javascript to calculate the actual width

Another solution is to use javascript to replace the classic scollbars with overlay scrollbars like you see on mobile operating systems.
[OverlayScrollbars](https://kingsora.github.io/OverlayScrollbars/) is a popular js library that does this.
