---
date: 2023-07-11
---

# Use the Chrome devtools recorder to automate UI testing

Chrome devtools has a pretty decent recorder feature that can record and playback your UI interactions.
It's currently in preview but it's been working well for me so far.

It's especially handy if you have to keep repeating the same 5 steps every time you reload the page to test your code.

It automatically waits for UI elements to load and it's pretty easy to tweak the recorded steps and export as a puppeteer script: https://developer.chrome.com/docs/devtools/recorder/

