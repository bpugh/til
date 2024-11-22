---
date: 2024-11-19
---

# Personal git ignore per repository

Today I learned that git has a `$GIT_DIR/info/exclude` file can contain additional patterns of files to ignore but isn't committed to the repository.

For me this is handy for some tooling configuration files that I use personally but don't want to clutter the main `.gitignore` of the repo.

If there are some files that you want to _always_ ignore, then you can specify a **global** ignore file in your git config with `core.excludesFile`.

[The official docs](https://git-scm.com/docs/gitignore) have a nice breakdown of when to use which method.

## Don't you want to be using the same tools as the rest of your team?

Great point!
For me it's usually specific editor config files that I have set in my global git ignore file since I'd never want them committed.
For example I use vim for certain things so I have these files ignored in `~/.gitignore_global`:
```
# Swap files
[._]*.s[a-v][a-z]
[._]*.sw[a-p]

# Session
Session.vim

# Temporary
*~
# Auto-generated tag files
tags
# Persistent undo
[._]*.un~

.vscode
.zed
```
I have `.vscode` in there as well since I occasionally find myself on teams where no one else uses it... and [Zed](https://zed.dev/) is really new but I've just been playing around with it.

For repo specific ignores in `$GIT_DIR/info/exclude`, it tends to be tools for managing environments like [Volta](https://volta.sh/) for node or [asdf](https://asdf-vm.com/) and [mise](https://mise.jdx.dev/) for other runtimes.

Also sometimes I find it useful to run some linting tools for myself when the rest of team hasn't bought into it yet.

For example, it took over a year with recent team to convince them add eslint to the project but in the mean time it was at least catching things for me in the editor with my own code or while reviewing PRs.

Likewise, I always have [cSpell](https://cspell.org/) running with Vscode to spell check my code so I have the `project-words.txt` file ignored.
I don't have these ignored globally since in some repos they do end up getting committed.

But I totally agree, you want to be cognizant of potential conflicts with the rest of the team depending on the tool.
Configuration for tools like code formatters should definitely be shared with the team. And trying to use something like `yarn` when the team is using `npm`, is asking for trouble.
