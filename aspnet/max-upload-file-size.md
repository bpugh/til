---
date: 2024-08-30
---

# ASP.NET max upload file size

Today I learned there are *two* configuration values that determine how large of a file can be uploaded.
`maxRequestLength` is specified in **Kilobytes** and it's used by the ASP.NET framework.
If the file is larger than this value then the application will throw "content length exceed" exception so it just comes back as a 500 which isn't that helpful.
The default is about 4mb.

`maxAllowedContentLength` is used by IIS and is specified in **bytes** not kilobytes and if the file is larger then it will return 413 error status which we can handle appropriately.
The default is about 28mb.

Both of these values need to set to larger than the file size we want to allow but in our case we needed the `maxAllowedContentLength` to be the smaller value so that an upload that's too large will always get rejected by IIS first so we can display a useful error message to the user.

The issue we ran into was if the file was more than 4mb but less than 28mb, it was reject by aspnet and throwing a 500 which in production comes back as a 302 redirect to the error page which we weren't handling so it would look like the upload was just hanging.

If the file was larger than 28mb then it would get rejected by IIS and return a 413 which we *were* handling so we would display the correct "File is too large" error message.

There are even more ways to limit upload size you read about in Kahlid's post: [increase file upload limit](https://khalidabuhakmeh.com/increase-file-upload-limit-for-aspdotnet)
