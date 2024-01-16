---
date: 2024-01-16
---

# Fix package-lock.json merge conflicts

Today I learned that npm can handle merge conflicts in your `package-lock.json` file for you.

After you resolve any merge conflicts in your `package.json`, you can just run `npm install [--package-lock-only]` and npm will resolve the conflicts in the lock file.
If `--package-lock-only` is provided, it will do this without also modifying your local `node_modules/`.

[Solving conflicts in package-lock.json](https://tkdodo.eu/blog/solving-conflicts-in-package-lock-json)