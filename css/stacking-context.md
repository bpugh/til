---
date: 2023-06-30
---

# Stacking context affects z-index

In CSS, the stacking context can impact which elements display on top of each in addition to the `z-index`. So if you end up in a situation where cranking up the `z-index` doesn't seem to work, the stacking context is likely the issue.
I technically learned this a while ago but completely forgot about it until I was just reminded about it by a coworker dealing with this issue.
Josh Comeau explains it well in his post on [stacking contexts](https://www.joshwcomeau.com/css/stacking-contexts/).
