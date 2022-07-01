# METAPROGRAMMING

## What is metaproramming?

The best collective term for the set of things that are more about process than about writing code or working more efficiently.
Systems for building and testing the code, and for managing dependencies.

It can also be phrased as [`programs that operate on programs`](https://en.wikipedia.org/wiki/Metaprogramming), but not quite right.

## Build Systems

Some sequence of operations that are required to go from inputs to the output, commonly termed as `build process`. Often ,these process have many steps, branches,etc. to generate resutls. So here comes tools, which help in making things less annoying while building somethings, usually called `**build system**`.

There are many of those,depending on the task at hand, language of preference, and the size of the project. At core, they all are same. 

We define, a number of *dependencies*, a number of *targets*, and *rules* for going from one to other.

### How does the build systen work?

You tell the build system, that you want a particular *target*, and its *job* is to find all the transitive dependencies of that target, and then apply the *rules* to produce the *intermediate targets* all the way until the *final target* has been produced. Ideally, the **build system** does this wihout unnecessarily executing rules for targets whose dependencies haven't changed and where the result is available from a previous build.

One such example of the build system is `make`. One of the most common build system, installed on almost every UNIX-system. It has it's cons, but it is works well till moderate projects.

When you run `make`, it consults a file called `MakeFile` in current directory. All the targets, their dependencies, and rules are defined in that file. Looking like -

```(MakeFile)
paper.pdf: paper.tex plot-data.png
	pdflatex paper.tex

plot-%.png: %.dat plot.png
	./plot.py -i $*.dat -o $@
```

Each directive in this file, is a rule to produce left-side using right-side.
On, phrased differently, the things named on the right-side of `:` are dependencies, and on left-side of `:` are target. In short meaning, make target with following dependencies.
Usually, the first directive defines the default goal. If you run `make`, with no arguements, this is the target it will build.

The `%` in a rule is *pattern*,and will match the same string on the left and on the right. For example, if target is `plot-foo.png` is requested, `make` will look for the dependencies `foo.dat` and `plot.png`. 

On running `make`, with an empty source directory

```(shell)
$ make

make: *** No rule to make target 'paper.tex', needed by 'paper.pdf'.  Stop.
```

`make` is telling us, in order to build `paper.pdf`, it needs `paper.tex`. and it has no rule telling it how to make that file. Let's do it again with some change !

```(shell)
$ touch paper.tex
$ make
make: *** No rule to make target 'plot-data.png', needed by 'paper.pdf'.  Stop.
```

It cannot make that file, due to pattern rule, and since the source file `data.dat` doesn't exist, so it tells the same.

So, let's try again  with these files -
- [paper.tex](https://github.com/IumoInfinium/missing_semester/blob/main/lecture8/paper.tex)
- [plot.py](https://github.com/IumoInfinium/missing_semester/blob/main/lecture8/plot.py)
- [data.dat](https://github.com/IumoInfinium/missing_semester/blob/main/lecture8/data.dat)

After making changes like above file, try running `make` again.
It will show the commands run in the order and a lot of exrta output while creating the target. And yeah, in this case, it made a PDF for us!!
On running, `make` again, it says the `target` is up to date.

> You will see a change in target, depending upon the change in the dependencies. Note, you will see it only after running `make` again.



## Dependency Management

At a macro level, a software project is likely to have more dependencies that are themselves projects, like `python`, `openssl` and libraries within the programming languages(like `matplotlib`).hese days, most dependencies will be available through a *repository* that hosts a large number of such dependencies in a single place, and provides a convenient mechanism for installing them.
Some examples are `PyPi` for python libraries, `apt` tool for Ubuntu-system packages, etc.

### Identifying Projects

**Versioning** - Most projects that other projects depend on issue a version number with every release. Usually something like 8.1.3 or 64.1.20192004. They are often, but not always, numerical. Version numbers serve many purposes, and one of the most important of them is to ensure that software keeps working. Imagine, for example, that I release a new version of my library where I have renamed a particular function. If someone tried to build some software that depends on my library after I release that update, the build might fail because it calls a function that no longer exists! Versioning attempts to solve this problem by letting a project say that it depends on a particular version, or range of versions, of some other project. That way, even if the underlying library changes, dependent software continues building by using an older version of my library.
Refer to this page for a generalized idea on versioning with [semantic versioning](https://semver.org/). It's in form of `<major-version-number>.<minor-version-number>.<patch-version-number>`.

**Lock Files** - A lock file is simply a file that lists the exact version you are currently depending on of each dependency. Usually, you need to explicitly run an update program to upgrade to newer versions of your dependencies.
An extreme version of this kind of dependency locking is vendoring, which is where you copy all the code of your dependencies into your own project. That gives you total control over any changes to it, and lets you introduce your own changes to it, but also means you have to explicitly pull in any updates from the upstream maintainers over time.
An extreme version of this kind of dependency locking is vendoring, which is where you copy all the code of your dependencies into your own project. That gives you total control over any changes to it, and lets you introduce your own changes to it, but also means you have to explicitly pull in any updates from the upstream maintainers over time.

## Continous Integration Systems

As you work on larger and larger projects, you’ll find that there are often additional tasks you have to do whenever you make a change to it. You might have to upload a new version of the documentation, etc..

**Continous Integration or CI** -is an umbrella term for “stuff that runs whenever your code changes”, and there are many companies out there that provide various types of CI, often for free for open-source projects. Some of the big ones are Travis CI, Azure Pipelines, and GitHub Actions.

### How they work?

You add a file to your repository that describes what should happen when various things happen to that repository. By far the most common one is a rule like “when someone pushes code, run the test suite”. When the event triggers, the CI provider spins up a virtual machines (or more), runs the commands in your “recipe”, and then usually notes down the results somewhere. You might set it up so that you are notified if the test suite stops passing, or so that a little badge appears on your repository as long as the tests pass.

### How the missing-semester

As an example of a CI system, the class website is set up using GitHub Pages. Pages is a CI action that runs the Jekyll blog software on every push to master and makes the built site available on a particular GitHub domain. This makes it trivial for us to update the website! We just make our changes locally, commit them with git, and then push. CI takes care of the rest.

### Side-Notes 

Most large software projects come with a “test suite”. You may already be familiar with the general concept of testing, but we thought we’d quickly mention some approaches to testing and testing terminology that you may encounter in the wild:

- **Test Suite** : A collective term for all the tests
- **Unit Test** : A "micro-test" that tests a specific feature in isolation.
- **Integration Test** : A "macro-test" to check all components of system work together.
- **Regression Test** : Testing a particular pattern that *previously* caused to bug, it is done to ensure that the bug does not resurface.
- **Mocking** : A fake implementation of a function, module, etc. to avoid testing unrelated functionality. Example - mock the network, mock the disk.
