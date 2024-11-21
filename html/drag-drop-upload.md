---
date: 2024-07-24
---

# Drag and drop upload

#til that creating a nice drag-and-drop file component using vanilla javascript and the built web APIs is actually fairly easy.

[Smashing Magazine](https://www.smashingmagazine.com/2018/01/drag-drop-file-uploader-vanilla-js/) has an easy-to-follow example.

The gist of it is that the browser gives you `'dragenter', 'dragover', 'dragleave'` events that you can use to style your "dropzone" however you want and the `drop` event allows you to handle the files themselves:

```js
dropArea.addEventListener('drop', handleDrop, false)

function handleDrop(e) {
  let dt = e.dataTransfer
  let files = dt.files

  // implement with your preferred upload method
  uploadFiles(files)
}
```

The `dragevent` and `dataTransfer` interface have been supported in modern browsers for some time so they are pretty safe to use.

Alternatively, if you don't care about styling a fancy drop area, the standard HTML `<input type="file">` element supports dragging a file onto it.

