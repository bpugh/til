---
date: 2023-09-25
---

# --update-refs won't update a ref if it's currently checked out in a working directory

Today I learned that if you're using the fairly new `--update-refs` feature of git to update multiple refs during a rebase, git won't update a ref if it's currently checked out in another working directory for that repo.

This makes sense but git currently doesn't give you any feedback that it wasn't updated or why. It wasn't until I tried to manually update it with a `git branch --force` that it told me the issue:

`fatal: cannot force update the branch 'feature-1' checked out at '/projects/my-other-branch'`

If you're not familiar with either of these features I highly recommend looking into them.
Andrew Lock has excellet write-ups on them:

* [Working on two git branches at once with git worktree](https://andrewlock.net/working-on-two-git-branches-at-once-with-git-worktree/)
* [Working with stacked branches in Git is easier with --update-refs](https://andrewlock.net/working-with-stacked-branches-in-git-is-easier-with-update-refs/)
