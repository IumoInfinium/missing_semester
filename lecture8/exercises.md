# EXERCISES 

1. Most makefiles provide a target called `clean`. This isn’t intended to produce a file called `clean`, but instead to clean up any files that can be re-built by make. Think of it as a way to “undo” all of the build steps. Implement a `clean` target for the `paper.pdf` `Makefile` above. You will have to make the target [phony](https://www.gnu.org/software/make/manual/html_node/Phony-Targets.html). You may find the [`git ls-files`](https://git-scm.com/docs/git-ls-files) subcommand useful. A number of other very common make targets are listed [here](https://www.gnu.org/software/make/manual/html_node/Standard-Targets.html#Standard-Targets).

    **Solution** : Check this files - [paper.tex](https://github.com/IumoInfinium/missing_semester/blob/main/lecture8/paper.tex), [plot.py](https://github.com/IumoInfinium/missing_semester/blob/main/lecture8/plot.py),[data.dat](https://github.com/IumoInfinium/missing_semester/blob/main/lecture8/data.dat),[makefile](https://github.com/IumoInfinium/missing_semester/blob/main/lecture8/makefile)

    After having these files on your system, try the following commands
    Articles you should go through, before trying them, [MakeFileTutorial](https://makefiletutorial.com/)

    ```(shell)
    Run makefile
    $ make
    ------lots of output-------

    $ ls
    data.dat  makefile  paper.aux  paper.log  paper.pdf  paper.tex  plot-data.png  plot.py

    $ xdg-open paper.pdf
    You will see a graph plotted on the paper

    $ make clean
    Undo the build - removes the file created by **make**

    $ls
    data.dat  makefile  paper.tex  plot-data.png  plot.py
    ```

2. Take a look at the various ways to specify version requirements for dependencies in [rust’s build system](https://doc.rust-lang.org/cargo/reference/specifying-dependencies.html). Most package repositories support similar syntax. For each one (caret, tilde, wildcard, comparison, and multiple), try to come up with a use-case in which that particular kind of requirement makes sense.
