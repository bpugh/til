---
date: 2023-09-19
---

# Specify timestamp in Google Drive video URL

Today I learned that Google Drive uses the same video player as YouTube so if you want to link to a specific timestamp in a video you can append a URL parameter like `t=<number of seconds>`.

So to share a link to a video and have it start playing at 10:44, the URL will look like `/view?t=644`.

A colleague also pointed out that you don't have to calculate the timestamp in seconds — the `t` parameter accepts a shorthand like so `t=10m44s`
