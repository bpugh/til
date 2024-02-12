---
date: 2024-02-12
---

# Git Maintenance

Today I learned about the [`git maintenance`](https://git-scm.com/docs/git-maintenance) command that runs tasks for regular maintenance of a git repo.

If you run `git maintenance start` in a repo, git will create scheduled tasks to run at regular intervals to perform these tasks in the background like garbage collection.
This will optimize and speed up the repo without having to tack them on occasionally as you run other commands.

A particularly handy task it will run every hour is `prefetch`, where it does a `git fetch` but only pulls down the data and doesn't update any refs.
Then when you actually run `git fetch` or `git pull`, it completes almost instantly because it already has all the data.

On Windows, you can view and tweak these tasks in the Task Scheduler and have names in the form of `Git Maintenance (<frequency>)`.

This also ties in well with my desire to be able to work offline if need be, since if I'm suddenly without internet but haven't been running fetch all day, I can still run `git fetch` and pull in all the changes from the day.