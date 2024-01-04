---
date: 2024-01-04
---

# Easily reference upstream branch

Today I learned that you can reference the upstream branch in git with `@{u}`.

I used this to make a convenient git alias `reso` for "reset to origin":

```bash
git config --global alias.reso "reset --keep @{u}"
```

note: I'm using `--keep` instead of `--hard` because it's a bit [safer](./reset-keep.md)

I use this when a branch I've pulled down has completely changed on the remote and I have no changes (for instance reviewing a PR) and a `pull` would be messy (this is also much faster depending on the number of commits).

Or if I've completely borked my local branch and want to start over from where I last pushed 😅.
