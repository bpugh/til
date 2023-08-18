---
date: 2023-08-16
---

# Git branch --force

Today I learned about the `--force` parameter of `git branch` which will take an existing branch and point it to a different commit.
This is another handy alternative to `git reset --hard` for some common scenarios.

For example, if I forgot to create a new feature branch and accidentally made some commits onto `main`, I can run the following:

``` bash
git checkout -b new-branch # create the new branch and switch to it
git branch --force main origin/main # fix main back to what it should be
```

vs what I would do before:

``` bash
git branch new-branch
git reset --hard origin/main
git checkout new-branch
```
which is one less command, but even better the contents of my working directory don't have to change at all!



