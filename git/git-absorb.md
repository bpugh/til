---
date: 2023-10-04
---

# git-absorb



One of my favorite git plugins is [git-absorb](https://github.com/tummychow/git-absorb) (which is a port of Mercurial's absorb).  
It basically helps you create `--fixup` commits automatically, which you can then use an interactive rebase with autoSquash to "absorb" them into your previous commits.

I tend to use it when I've made a bunch of small tweaks to my feature branch, especially from automated feedback from a PR bot, I'll then stage the changes and [git-absorb](https://github.com/tummychow/git-absorb) will find the previous commit on my branch that also modified those same lines.

I have a git alias set to run:
`git absorb --base main --force`  
So it'll search through all the commits on my branch whether I've pushed them or not.

As usual Andrew Lock has the best post explaining it: (https://andrewlock.net/super-charging-git-rebase-with-git-absorb/)
