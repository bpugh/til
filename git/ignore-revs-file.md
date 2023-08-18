---
date: 2023-08-17
---

# Ignore commits in Git Blame with --ignore-revs-file

Today I learned that you can ignore commits in Git blame on Github with a `.git-blame-ignore-revs` file in the root of your repo!

I'd known about the `git config blame.ignoreRevsFile` config option where you can point it to a file with a list of commit IDs to ignore which is especially useful for those annoying commits in a repo where whitespace was cleaned up or every tab in the codebase was replaced with spaces.
You have to run the [config command locally](https://www.stefanjudis.com/today-i-learned/how-to-exclude-commits-from-git-blame/) but now apparently [Github does it automatically](https://docs.github.com/en/repositories/working-with-files/using-files/viewing-a-file#ignore-commits-in-the-blame-view).

I also learned you can include comments in the file like:

```
# Run this command to always ignore formatting commits in `git blame`
# git config blame.ignoreRevsFile .git-blame-ignore-revs

# Changed everything to tabs
a926bba49c89a5b882cd298be3af2570b1e6252c

# Fixed all the formatting errors
5e78fdc6eac01e4e730046dc2811fbb78157a154
```
