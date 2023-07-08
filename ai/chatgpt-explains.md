---
date: 2023-07-05
---

# Use ChatGPT to explain bash scripts

Today I learned that chatGPT is pretty good at explaining cryptic bash scripts and commands.
I was trying to understand exactly how a git `prepare-commit-msg` hook was working so I asked chatGPT to "explain the following git hook to me" and it did a pretty good job.

For example, it returned tidbits like:

`[[ $BRANCH_NAME =~ $BRANCH_REGEX ]]`: This conditional statement checks if the branch name matches the BRANCH_REGEX pattern.
If the branch name starts with one or more digits, this condition will be true.
and:
`sed -i.bak -e "1s/^#${BASH_REMATCH[1]}: //I" $1`: This line uses the `sed` command to replace the branch number (captured by the `BRANCH_REGEX` pattern) and a colon at the beginning of the commit message with an empty string. The `I` flag makes the replacement case-insensitive. The `-i.bak` option creates a backup of the original commit message file with a `.bak` extension.

*Bonus TIL*: the `BASH_REMATCH` variable is automatically populated with the matched string in bash when using the `=~` regex operator
