---
date: 2023-08-09
---

# Git reset --keep

I just learned that `git reset` has a `--keep` parameter.
This works the same as `--hard` except that it won't discard any uncommitted changes.
It's meant to be used when we want to remove some of the last commits in the current branch but if there could be conflicts between the changes in the commits we want to remove and our uncommitted changes, then the reset is blocked.

I'd been using `git reset --hard` and just double checking I didn't have anything uncommitted but I'll be defaulting to `--keep` except if I'm intentionally trying to clear out my changes.
