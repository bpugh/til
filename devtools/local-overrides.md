---
date: 2023-12-11
---

# Local overrides in Chrome DevTools

Today I learned about the [local overrides](https://developer.chrome.com/docs/devtools/overrides) feature of Chrome Devtools that lets you "you can override HTTP response headers and web content, including XHR and fetch requests, to mock remote resources even if you don't have access to them".

This came in handy for me when trying to debug an issue that I wasn't able to reproduce locally. The official docs do a nice job showing how to enable the feature but just make sure you delete the override once you're done otherwise you might wonder why the page has stopped updating.

https://developer.chrome.com/docs/devtools/overrides
