---
date: 2024-08-20
---

#

This is a simple thing but I just discovered that with a simple regex and find/replace in most editors, you can quickly add text to the end of every line.

For instance, if you want to add a `,` to every line, all you need is `$`:

![alt text](image.png)

Or if you want to replace whatever the last character then you can use `.$` instead.

Of course I use [vscode-neovim](https://github.com/vscode-neovim/vscode-neovim) so I just type `:%s/$/,/` 😁
