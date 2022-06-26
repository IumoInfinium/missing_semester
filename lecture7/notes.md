# DEBUGGING AND PROFILING

## Debugging

Normal print statements can be used to debug programs, but there is a more efficient way to do so, that is using `logs`. The pros of using it are :
- Errors or problems can be classified in 5 different levels, namely - `INFO`,`DEBUG`,`WARNING`,`ERROR` and `CRITICAL`.
- These levels have priorities !
- Saves precious time from debugging ^_^

> An example of it can be found in [logger.py](). Execute it using python simply and also with an additional parameter **color**.
	```(python)
	python3 logger.py
	python3 logger.py color
	```

If you see a difference, go to below topic to know more.

### Color Coding Characters in Shell:echoe "Use h"

Since we know shell is made up of characters! We can add up some colorful characters to it.
Example :
	` printf "\e[38;2;255;0;0m This is in red \e[0m"`

Now, What it does is, the numbers here are ANSI color escape codes, refer [here](https://gist.github.com/fnky/458719343aabd01cfb17a3a4f7296797) to know more.

For this example, we did red color for text, with following -
- 38 for changing the foreground color.
- 2 for the color format, means the text format is normal.(not bold and bright)
- 255;0;0 sets the foreground text with `r`;`g`;`b`;

Check out the script to show different colors in terminal [script here]()

### Logs

Most systems and programs use logs for almost everything.
GNU has logs in `/var/log`

Here comes the term - `Centralized Logging`, means having a common area for securely storing logs.

### Debugger

Debuggers are programs that let you interact with the execution of a program, allowing the following:

- Halt execution of the program when it reaches a certain line or when it mets a certain condition.
- Step through the program one instruction at a time.
- Inspect values of variables after the program crashed.
- And many more features !!!

Many programming languages come with some form of debugger. Some examples of debugger are -

- `pdb` A python debugger, which can be used using `python -m pdb someFileToDebug.py`.

> A more advanced version of `pdb` is `ipdb` which suppports syntax hightlighting, tab completion, etc...

- `gdb` A debugger for c-like languages(c,c++,etc..). It is a low-level debugger. It can be used using `gdb --args sleep 20`.

### Specialized Tools

Say, you have a python program for a certain math calculation, but your program for some reason uses the file stream, so how do you know this has occured?
We can check system calls to check for a occurance of a certain event.

In GNU, `strace` is used to check syscalls. And in MacOS and  BSD use `dtrace` for it. ``dtrave`` is tricky tool since it has its own `D` language. But fortunately, a wrapper `dtruss` is there, to provide a more similar interface to `strace`.

```(shell)
# On Linux
sudo strace -e lstat ls -l > /dev/null
4
# On macOS
sudo dtruss -t lstat64_extended ls -l > /dev/null
```

### Static Analysis Tool

Imagine, a case where you have a syntatical error in a program, so instead of running the whole program, we can error check it with some tools.
These tools use source code as input and output the errors i.e. check its correctness.
Also called linters.

Some tools -

- One such tool is `pyflakes`. It shows the erros in source code without running the code.
- Text Editors, like `vim` can use these linters to show errors at code-making.
- In web development, the `inspect` option in browsers is a debugging tool.

## Profiling

Help you understand which parts of your program are taking most of the time and/or resources so you can focus on optimizing those parts

Different time in process :

- **Real time** -Time taken by other processes and time taken while blocked (e.g. waiting for I/O or network)

- **User time** - Amount of time spent in the CPU running user code

- **System time** - Amount of time spent in the CPU running kernel code

Example :

```(shell)
$ time curl https://missing.csail.mit.edu &> /dev/null
~real    0m2.561s
~user    0m0.015s
~sys     0m0.012s
```

### Profilers

Most of the time when people refer to profilers they actually mean CPU profilers, which are the most common. There are two main types of CPU profilers:

- **Tracing** and **Sampling** Profilers : Keeps a record of every function call your program makes whereas sampling profilers probe your program periodically (commonly every millisecond) and record the program’s stack. They use these records to present aggregate statistics of what your program spent the most time doing. A [good](https://jvns.ca/blog/2017/12/17/how-do-ruby---python-profilers-work-) article.

Example : In python, we have `cProfile`,to profile time per function call.

```(shell)
python -m cProfile -s tottime grep.py 1000 '^(import|\s*def)[^,]*$' *.py
```

### Line Profiler

A more intuitive way of displaying profiling information is to include the time taken per line of code, which is what line profilers do.

### Memory Profiler

In languages like C or C++ memory leaks can cause your program to never release memory that it doesn’t need anymore. To help in the process of memory debugging you can use tools like Valgrind that will help you identify memory leaks.
In garbage collected languages like Python it is still useful to use a memory profiler because as long as you have pointers to objects in memory they won’t be garbage collected.

### Event Profiling

As it was the case for strace for debugging, you might want to ignore the specifics of the code that you are running and treat it like a black box when profiling.
Here comes, `perf` command, abstracts CPU differences away and does not report time or memory, but instead it reports system events related to your programs. For example, perf can easily report poor cache locality, high amounts of page faults or livelocks. Here is an overview of the command.

```(shell)
sudo perf <stat><list><record><report> stress -c 1
```

### Visualization

1. [Flame Graph](http://www.brendangregg.com/flamegraphs.html),which will display a hierarchy of function calls across the Y axis and time taken proportional to the X axis. They are also interactive, letting you zoom into specific parts of the program and get their stack traces.

2. [Call Graph](https://upload.wikimedia.org/wikipedia/commons/2/2f/A_Call_Graph_generated_by_pycallgraph.png) or control flow graphs display the relationships between subroutines within a program by including functions as nodes and functions calls between them as directed edges. When coupled with profiling information such as the number of calls and time taken, call graphs can be quite useful for interpreting the flow of a program. In Python you can use the pycallgraph library to generate them.

## Resouce Monitoring

- **General Monitoring**- `htop` presents various statistics for the currently running processes on the system. `dstat` is another nifty tool that computes real-time resource metrics for lots of different subsystems like I/O, networking, CPU utilization, context switches, &c.

- **I/O operations** - `iotop` displays live I/O usage information.

- **Disk Usage** - `df` displays metrics per partitions and `du` displays disk usage per file for the current directory. A more interactive version of `du` is `ncdu`.

- **Memory Usage** - `free` displays the total amount of free and used memory in the system.

- **Open Files** - `lsof` lists file information about files opened by processes.

- **Network Connections and Config** - `ss` lets you monitor incoming and outgoing network packets statistics as well as interface statistics.

- **Network Usage** - `nethogs` and `iftop` are good interactive CLI tools for monitoring network usage.

### Specialized Tools

Tools like `hyperfine` let you quickly benchmark command line programs. For instance, in the shell tools and scripting lecture we recommended `fd` over `find`. We can use hyperfine to compare them in tasks we run often. E.g. in the example below fd was 20x faster than find in my machine.

```(shell)
hyperfine --warmup 3 'fd -e jpg' 'find .-iname "*.jpg"'
```
