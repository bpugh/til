---
date: 2024-05-21
---

# BFCache

Today I learned that the Backwards/forwards cache (BFCache) is a thing.
This is the cache where the browser keeps a snapshot of a webpage so that it's able to display almost instantly when a user clicks the back or forward buttons.

This post gives a nice [overview of the BFCache](https://www.sabatino.dev/bfcache-explained/) and how it works — apparently "Chrome usage data shows that 1 in 10 navigations on desktop and 1 in 5 on mobile are either back or forward".

The Chrome Devtools also has a feature to let you [test if your page is cacheable] in the BFCache.
