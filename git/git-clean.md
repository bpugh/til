---
date: 2024-01-23
---

# Git clean interactive

I just discovered the interactive mode of `git clean`.

Git Clean is handy when you want to clear out anything from your local repository folder that isn't tracked by git. This often includes build outputs and other generated files. This is useful if for instance Visual Studio is acting weird and you're tempted to do a fresh clone to fix it.

I have a git alias I use for this: `cl = git clean -idx -e 'node_modules'`

This tells git to delete any untracked files including anything ignored by `.gitignore` so it's practically the same as doing a fresh clone (except you'll keep work in progress). The `-i` is interactive so git shows you everything it'll delete and you can confirm it. I used to use `-f` for force but the interactive mode is pretty nice and it's just a couple of extra keystrokes to blow everything way if I want.

The `-e 'node_modules'` is optional but if it's a dotnet build issue I'm having then I don't want to waste time deleting and reinstalling npm modules so this tells git not to touch any `node_modules` in the repo.