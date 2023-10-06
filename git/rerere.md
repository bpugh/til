---
date: 2023-10-05
---

# Git rerere

If you've ever had to abort a rebase or merge but didn't want to waste the work you already did resolving merge conflicts, then you should enable the git rerere option:

`git global config rerere.enabled true`

It stands for Reuse Recorded Resolution, and it essentially remembers how you resolved a merge conflict and will automatically reapply it sees it again.

[Resolving conflicts with git-rerere](https://bitbucket.org/blog/resolving-conflicts-with-git-rerere)
