---
date: 2023-08-07
---

# Git pickaxe

You can search through git history not only by the text of a commit message but by the _contents of the diff_ of commits.
This is commonly referred to as the [git pickaxe](http://www.philandstuff.com/2014/02/09/git-pickaxe.html) and you invoke it with the `-S` parameter to `git log` i.e. `git log -S 'public void SomeMethod` and you'll get every commit that touched that method signature or even one that _deleted_ it.

Some git clients will expose this as an option in a search field but if that fails the git cli lets you include additional filters like author or file path or even use regex with the `--pickaxe-regex` switch.

[See an example](http://www.philandstuff.com/2014/02/09/git-pickaxe.html)
