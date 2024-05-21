---
date: 2024-05-20
---

# Locally test on old version of Chrome

Today I learned that if you need to test in older versions of Chrome then you can [download prior snapshots of Chromium builds](https://commondatastorage.googleapis.com/chromium-browser-snapshots/index.html) as standalone executables.

The tricky part is figuring out which build snapshot corresponds to which version of Chrome, which involves several steps detailed in the [Chromium wiki](https://www.chromium.org/getting-involved/download-chromium/#downloading-old-builds-of-chrome-chromium).

Fortunately, someone put together a site to [lookup by Chrome version](https://vikyd.github.io/download-chromium-history-version/#/) and link to the correct build on the archive site.
Then you download and extract the zip file and run the single executable, i.e. `chrome.exe`.

