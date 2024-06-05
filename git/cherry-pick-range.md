---
date: 2024-06-04
---

# Cherry pick a range of commits

I just recently learned that you can actually cherry pick a range of commits instead of just a single commit:

```bash
git cherry-pick c1..c3
```
The above is using the two-dot range notation (`..`).

I was a bit surprised by this because I thought that this was the purpose of `rebase --onto` — to take a series of commits and apply them one at a time on top of some other commit.

Turns out that they both essentially do the same thing (for each commit they call `merge-base` under the hood and apply a [3-way merge](https://jvns.ca/blog/2023/11/10/how-cherry-pick-and-revert-work/) though you can also think of rebase as a series of cherry picks) but one can be more convenient than the other depending on what you're doing or how you prefer to think of the operation.

Cherry-pick is more convenient if you want to take a series of commits from some _other_ branch and apply them onto the _current_ branch.

Rebase is more convenient if you want to take the _current_ branch and apply it on top of some _other_ branch.
And with the `--onto` parameter you can change the base or "parent branch".
This is a bit harder to wrap your head around extremely powerful.

For example given the following:

```
                        H---I---J topicB
                        /
              E---F---G  topicA
              /
A---B---C---D  main
```
If you run `git rebase --onto master topicA topicB` then you end up with:

```
              H'--I'--J'  topicB
            /
            | E---F---G  topicA
            |/
A---B---C---D  main
```

which is handy if you started working on `topicB` and thought you were branched off of `main` instead of `topicA` or if `topicA` got merged or squashed from under you.
This [SO answer](https://stackoverflow.com/a/29916361/1715138) does a great job explaining `--onto`.

Just remember: `git rebase --onto <newparent> <oldparent> <until>`

To accomplish the same with cherry-pick would require something like:
```bash
git checkout main
git branch -b temp # create a new temp branch and switch to it
git cherry-pick topicA..topicB
git checkout topicB
git reset --hard temp # topicB is now updated to match temp
git branch --delete temp
```


