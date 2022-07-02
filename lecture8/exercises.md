# EXERCISES 

1. Most makefiles provide a target called `clean`. This isn’t intended to produce a file called `clean`, but instead to clean up any files that can be re-built by make. Think of it as a way to “undo” all of the build steps. Implement a `clean` target for the `paper.pdf` `Makefile` above. You will have to make the target [phony](https://www.gnu.org/software/make/manual/html_node/Phony-Targets.html). You may find the [`git ls-files`](https://git-scm.com/docs/git-ls-files) subcommand useful. A number of other very common make targets are listed [here](https://www.gnu.org/software/make/manual/html_node/Standard-Targets.html#Standard-Targets).

    **Solution** : Files required, [paper.tex](https://github.com/IumoInfinium/missing_semester/blob/main/lecture8/paper.tex), [plot.py](https://github.com/IumoInfinium/missing_semester/blob/main/lecture8/plot.py),[data.dat](https://github.com/IumoInfinium/missing_semester/blob/main/lecture8/data.dat),[makefile](https://github.com/IumoInfinium/missing_semester/blob/main/lecture8/makefile)

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

    **Solution** : Various version requirements in Rust-build system are a follows...
    
    - *Caret Requirements* - Caret requirements are an alternative syntax for the default strategy, ^1.2.3 is exactly equivalent to 1.2.3. Example, a version number for a library.

    - *Tilde Requirements* - Specify a minimal version with some ability to update. If you specify a major, minor, and patch version or only a major and minor version, only patch-level changes are allowed. If you only specify a major version, then minor- and patch-level changes are allowed.

        `~1.2.3` is an example of a tilde requirement.
        ```(text)
        ~1.2.3  := >=1.2.3, <1.3.0
        ~1.2    := >=1.2.0, <1.3.0
        ~1      := >=1.0.0, <2.0.0
        ```
    
    - *Wildcard Requirements* - Wildcard requirements allow for any version where the wildcard is positioned.

        `*`, `1.*` and `1.2.*` are examples of wildcard requirements.
        ```(text)
        *     := >=0.0.0
        1.*   := >=1.0.0, <2.0.0
        1.2.* := >=1.2.0, <1.3.0
        ```

    - *Comparison requirements* - omparison requirements allow manually specifying a version range or an exact version to depend on.

        Here are some examples of comparison requirements:
        ```(text)
        >= 1.2.0
        > 1
        < 2
        = 1.2.3
        ```

    - *Multiple requirements* - As shown in the examples above, multiple version requirements can be separated with a comma, e.g., `>= 1.2`,`< 1.5`.

3. Git can act as a simple CI system all by itself. In `.git/hooks` inside any git repository, you will find (currently inactive) files that are run as scripts when a particular action happens. Write a [`pre-commit`](https://git-scm.com/docs/githooks#_pre_commit) hook that runs `make paper.pdf` and refuses the commit if the make command fails. This should prevent any commit from having an unbuildable version of the paper.

    **Solution** - Here is the file, analyze it and save it in `.git/hooks/pre-commit`. Remember, the files in `.git/hooks` are not Version Controlled!
    It is just a normal script file with a *particular* name, for hooks everything depends upon the *exit status*, if this case of `pre-commit`, if *exit status != 0` commit will not run, else commit runs.
    
    Only on running `git commit` you will notice the change.
    ```(script)
    #!/usr/bin/bash

    # Hook for running 'make' before commits, and if it fails, abort the commit as well.
    echo "Starting to execute 'make' command"
    LIGHTGREEN='\033[1;32m'
    LIGHTRED='\033[1;31m'
    NOCOLOR='\033[0m'
    if ($(make > output 2>&1)); then
       	    echo -e "${LIGHTGREEN}Successfully passed the pre-commit test${NOCOLOR}"
	    exit 0
    else
	    echo "${LIGHTRED}Error : Not able to run 'make'${NOCOLOR}"
	    exit 1
    fi
    ```

4. Set up a simple auto-published page using [GitHub Pages](https://pages.github.com/). Add a [GitHub Action](https://github.com/features/actions) to the repository to run shellcheck on any shell files in that repository (here is [one way to do it](https://github.com/marketplace/actions/shellcheck)). Check that it works! 


