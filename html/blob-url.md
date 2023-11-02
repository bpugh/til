---
date: 2023-11-02
---

# Blob URLs

Today I learned that in a web page, when you're working with Blob or File objects you can call `URL.createObjectURL()` to create a Blob URL that can be used as the source for anything that normally takes a URL like images or download links.

It's also apparently a good alternative to base64 encoded Data-URIs especially when dealing with larger amounts of data since a base64 encoded file will be 33% larger than the raw binary.

I was running into issues trying to embed a large PDF with the `<object>` element and instead of setting a massive base64 string as the data source, I was able to convert it to a blob and use a blob url so it ends up looking something like:

`<object data="blob:https://localhost/d827ea99-9e80-496a-a8e0-e107b83080e9" type="application/pdf"></object>`
