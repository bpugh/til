---
date: 2023-11-27
---

# Trim videos without re-encoding

Today I learned that [FFmpeg](https://ffmpeg.org/) is the easiest (only?) way to trim/cut a video without re-encoding it.

You can specify a start and stop time like so:

```bash
ffmpeg -i input.mp4 -ss 00:01:30.000 -to 00:04:05.000 -c copy output.mp4
```

The key is the `-c copy` parameter which will just copy the data frames for operations where they don't need to be modified.
This is nice because it's _way_ faster than decoding and re-encoding and you don't have any loss in quality if you're not working with a raw format.

It also works for removing/replacing the audio of a video.
This [ultimate guide](https://img.ly/blog/ultimate-guide-to-ffmpeg/#cut-and-trim-without-reencoding) is really handy.

