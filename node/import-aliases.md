---
date: 2023-11-08
---

# Native node import path aliases

Today I learned that node natively supports import path aliases with the [imports field](https://nodejs.org/api/packages.html#imports) in `package.json`.

The nice thing about this is that they're supported by most node tools now so you don't need to configure your aliases separately in different tools like eslint, webpack, vite, etc...

If you're not familiar with import aliases, they're a handy way to avoid unwieldy relative import paths.

instead of:
```js
import utils from '../../../../shared/utils';
```
you can have:

```js
import utils from '#shared/utils';
```

A nice config to start with is something similar to:

```json
"imports": {
    "#*": "./*"
  },
```
which lets you import anything from the root of your project.

I actually discovered this from looking through the [decision log](https://github.com/epicweb-dev/epic-stack/blob/main/docs/decisions/031-imports.md) of the [`epic-stack`](https://github.com/epicweb-dev/epic-stack) react project.

Unfortunately typescript doesn't support it yet (though it's planned), so you'd still need to update `tsconfig.json` with:

```json
"paths": {
      "#*": ["./*"],
},
```
