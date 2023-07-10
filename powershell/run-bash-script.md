---
date: 2023-07-09
---

# Run a bash script from Powershell

You can execute a bash script from Powershell on Windows by typing `bash` if you've enabled WSL.
For example `bash ./new-til.sh`. Some caveats though:

* Make sure you use `/` instead of `\` in the file path
* Make sure the bash script was saved with unix line-endings

You can also make a wrapper script for scripts you regularly execute like `new-til.ps1`:

``` powershell
bash ./new-til.sh $args
```

If you don't or can't enable WSL, you can use `sh.exe` that's optionally installed with Git for Windows.
For example `sh ./new-til.sh`

See this [StackOverflow post](https://stackoverflow.com/questions/1098786/run-bash-script-from-windows-powershell) for more caveats/solutions.
