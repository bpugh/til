---
date: 2024-11-21
---

# Selectively restoring changes from another branch or commit

#til that you can use the `--patch` parameter with several git commands.

The `--patch` parameter is probably most known for interactively staging changes from the cli, but I've never really used it because I find GUI clients are much more convenient for this.

But apparently you can also use it with restore/checkout to grab specific changes from another branch.
```bash
git restore --source=branch-name --patch
```

This is something I haven't seen easily done in any git client.

See [Tekin's post it](https://tekin.co.uk/2024/08/the-many-uses-for-git-patch) for more details and other uses.
