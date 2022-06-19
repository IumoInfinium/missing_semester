# Exercises

1. If you don’t have any past experience with Git, either try reading the first couple chapters of [Pro Git](https://wwww.git-scm.com/book/en/v2) or go through a tutorial like [Learn Git Branching](https://www.learngitbranching.js.org). As you’re working through it, relate Git commands to the data model.

    >Go through the Pro-Git Book and learn from the visual tutorial at git branching website

2. Clone the repository for the class [website](https://github.com/missing-semester/missing-semester).

    1) Explore the version history by visualizing it as a graph.

        > git log --graph --oneline --all

    2) Who was the last person to modify `README.md`? (Hint: use `git log` with an argument).

        > git log -1 README.md

    3) What was the commit message associated with the last modification to the
       `collections:` line of `_config.yml`? (Hint: use `git blame` and `git
       show`).

       > git blame _config.yml | grep collections: | cut -d ' ' -f 1 | git show -s --format=%s

3. One common mistake when learning Git is to commit large files that should
   not be managed by Git or adding sensitive information. Try adding a file to
   a repository, making some commits and then deleting that file from history
   (you may want to look at
   [this](https://help.github.com/articles/removing-sensitive-data-from-a-repository/)).

    > Can be done using a tool named git-filter-repo.Check out the article to know more

4. Clone some repository from GitHub, and modify one of its existing files.
   What happens when you do `git stash`? What do you see when running `git log
   --all --oneline`? Run `git stash pop` to undo what you did with `git stash`.
   In what scenario might this be useful?

   ```(git)
   1. Cloned a repositry and changed an existing file.
   2. Execute - git status, we see a file has been modified.
   3. Execute - git stash, modified file has been stashed(moved to a new git object, separate from current object).
   4. On executing, git log --oneline --all, shows the stashed commit
   5. Execute - git stash pop, returns the stashed commit
   ```

5. Like many command line tools, Git provides a configuration file (or dotfile)
   called `~/.gitconfig`. Create an alias in `~/.gitconfig` so that when you
   run `git graph`, you get the output of `git log --all --graph --decorate
   --oneline`. Information about git aliases can be found [here](https://git-scm.com/docs/git-config#Documentation/git-config.txt-alias).

   **Solution** : There are two ways to do it,open gitconfig and change it,or command to directly append it to gitconfig.

    1. Adding the following lines to gitconfig.

   ```(text)
    [alias]
            graph = log --all --oneline --graph --decorate
   ```

    2. Using the command

    > git config --global alias.graph "log --all --oneline --graph --decorate"

6. You can define global ignore patterns in `~/.gitignore_global` after running
   `git config --global core.excludesfile ~/.gitignore_global`. Do this, and
   set up your global gitignore file to ignore OS-specific or editor-specific
   temporary files, like `.DS_Store`.

   **Solution** :
    1. Execute `git config --global core.excludesfile ~/.gitignore_global`
    2. Now, create a file `gitignore_global` in `~/`
    3. Add the files/patterns in the file *gitignore_global* for git to ignore.

7. Fork the [repository for the class
   website](https://github.com/missing-semester/missing-semester), find a typo
   or some other improvement you can make, and submit a pull request on GitHub
   (you may want to look at [this](https://github.com/firstcontributions/first-contributions)).

    **Solution** : Gnerate a pull request on missing-semester github repo.