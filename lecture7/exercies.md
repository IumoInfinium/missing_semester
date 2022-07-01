# Exercies

## Debugging

1. Use `journalctl` on Linux or `log show` on macOS to get the super user accesses and commands in the last day. If there aren’t any you can execute some harmless commands such as `sudo ls` and check again.

```(shell)
journalctl -S yyyy-mm-dd
```

2. Do [this](https://github.com/spiside/pdb-tutorial) hands on `pdb` tutorial to familiarize yourself with the commands. For a more in depth tutorial read [this](https://realpython.com/python-debugging-pdb).

```(text)
Just do the pdb tutorial and find the problems and fix them
```

3. Install [`shellcheck`](https://www.shellcheck.net/) and try checking the following script. What is wrong with the code? Fix it. Install a linter plugin in your editor so you can get your warnings automatically..

```(shell)
#!/bin/sh
## Example: a typical script with several problems
for f in $(ls *.m3u)
do
  grep -qi hq.*mp3 $f \
    && echo -e 'Playlist $f contains a HQ file in mp3 format'
done
```
Solution :

```(shell)
shellcheck scriptName.sh
```

4. (Advanced) Read about [reversible debugging](https://undo.io/resources/reverse-debugging-whitepaper/) and get a simple example working using [`rr`](https://rr-project.org/) or [`RevPDB`](https://morepypy.blogspot.com/2016/07/reverse-debugging-for-python.html)..

Solution :

```(shell)
Go through the links and try to accomplish so.
```

## PROFILING

1. [Here](https://missing.csail.mit.edu/static/files/sorts.py) are some sorting algorithm implementations. Use [`cProfile`](https://docs.python.org/3/library/profile.html) and [`line_profiler`](https://github.com/pyutils/line_profiler) to compare the runtime of insertion sort and quicksort. What is the bottleneck of each algorithm? Use then `memory_profiler` to check the memory consumption, why is insertion sort better? Check now the inplace version of quicksort. Challenge: Use `perf` to look at the cycle counts and cache hits and misses of each algorithm

Solution :
```(shell)
# For cProfile
python -m cProfile -s tottime sort.py

# For line_profiler
python -m line_profiler sort.py

# For memory_profiler
 python -m memory_profiler sorts.py  

# Need to check for the perf cmd. [TO DO]

```

2. Here’s some (arguably convoluted) Python code for computing Fibonacci numbers using a function for each number.

```(python)
#!/usr/bin/env python
def fib0(): return 0

def fib1(): return 1

s = """def fib{}(): return fib{}() + fib{}()"""

if __name__ == '__main__':

    for n in range(2, 10):
        exec(s.format(n, n-1, n-2))
    # from functools import lru_cache
    # for n in range(10):
    #     exec("fib{} = lru_cache(1)(fib{})".format(n, n))
    print(eval("fib9()"))
```
Solution :

Put the code into a file and make it executable. Install prerequisites: [`pycallgraph`](http://pycallgraph.slowchop.com/en/master/) and [`graphviz`](http://graphviz.org/). (If you can run `dot`, you already have GraphViz.) Run the code as is with `pycallgraph graphviz -- ./fib.py` and check the `pycallgraph.png` file. How many times is `fib0` called?. We can do better than that by memoizing the functions. Uncomment the commented lines and regenerate the images. How many times are we calling each `fibN` function now?

```(shell)
Install the dependencies - pycallgraph, graphviz.
Executing the cmd - **pycallgraph graphviz -- ./fib.py**, gives output image and 34 as output.
With **fib0** being called 34 times according to the generated graph in image.

On changing the fibonacci program to memoization, the number of calls decreases, leading to a more efficient way  to do so.
And now the **fibn** executes only one time according.
```

3. A common issue is that a port you want to listen on is already taken by another process. Let’s learn how to discover that process pid. First execute `python -m http.server 4444` to start a minimal web server listening on port `4444`. On a separate terminal run `lsof | grep LISTEN` to print all listening processes and ports. Find that process pid and terminate it by running `kill <PID>`.

Solution :

```(shell)
# A temporary local web-server is created
$ python http.server 4444

# Get all the listening ports and processes
$ lsof | grep LISTEN

# Killing the process after finding the **pid** from last command
$ kill -9 <PID>
```

4. Limiting processes resources can be another handy tool in your toolbox. Try running `stress -c 3` and visualize the CPU consumption with `htop`. Now, execute `taskset --cpu-list 0,2 stress -c 3` and visualize it. Is `stress` taking three CPUs? Why not? Read [`man taskset`](https://www.man7.org/linux/man-pages/man1/taskset.1.html). Challenge: achieve the same using [`cgroups`](https://www.man7.org/linux/man-pages/man7/cgroups.7.html). Try limiting the memory consumption of stress -m.

Solution :

```(shell)
$ stress -c 3
# Running stress increase the load on cpu with 3 new dummy processes.

# Visualize the current load on system with htop[ open the htop window on separate window to monitor the changes][ TIP -tmux]
$ htop

# Trying this again in a different way, check the no. of processes of stress to compare
$ taskset --cpu-list 0,2 stress -c 3
```

> You would have found an extra stress process on running **htop** again! The reason for it is, the process hierarachy in the GNU-based systems, you can see the same in `htop` when changed to **tree** mode by pressing `F5`. Now, try running some more processes, and see how this affects the system with `htop` again. Here are few things, you can read to know more - [Process](https://www.usna.edu/Users/cs/bilzor/ic411/calendar.php?type=class&event=6), [Process Hierarchy](https://gist.github.com/CMCDragonkai/f58afb7e39fcc422097849b853caa140)

> Note : I need to learn more about Control Groups to complete the given question fully.

5. (Advanced) The command curl `ipinfo.io` performs a HTTP request and fetches information about your public IP. Open [Wireshark](https://www.wireshark.org/) and try to sniff the request and reply packets that curl sent and received. (Hint: Use the `http` filter to just watch HTTP packets).

```(shell)
# Returns some of your network information
$ curl ipinfo.io

# Now check the transmission packets with **WireShark**, hint in the question.
# You will notice outgoing and incoming packets, try to goof around to know some of the basics.
```
