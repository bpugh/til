---
date: 2023-09-13
---

# Mock service worker

I recently discovered [Mock Service Worker](https://mswjs.io/), a clever javascript utility that let's you mock your API by intercepting network requests.
I've started using it in my frontend tests after reading Kent's article [Stop Mocking Fetch](https://kentcdodds.com/blog/stop-mocking-fetch) and it's a nice way to test a component is handling network requests appropriately without actually hitting an API.
The novel aspect is that it can install itself as a service worker (which can intercept network requests for caching) in your app during development and reuse the same mock requests that you've setup during testing.
Handy for when the backend isn't ready or you don't want to take the time to get the app in the correct state to test a UI change.
