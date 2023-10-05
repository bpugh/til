---
date: 2023-10-03
---

# push.autoSetupRemote

Today I learned about the git config setting `push.autoSetupRemote` that was added in version 2.37.0.

Like [Tekin mentions in his post](https://tekin.co.uk/2020/01/git-alias-to-push-and-set-upstream-trackng-on-a-branch), I've had a git alias to do create my upstream branch but I still forget sometimes.
To me this seems safe to enable by default with:

`git config --global --add --bool push.autoSetupRemote true`

and git will now set the upstream tracking branch for you!

