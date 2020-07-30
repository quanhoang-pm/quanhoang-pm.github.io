---
title: "Visualize profiling result in Python"
date: 2020-07-30
last_modified_at: 2020-07-30 21:30:00
categories:
  - programming
tags:
  - Python
  - profile
---

Optimizing your program is important. However, knowing where to optimize differentiate good developers and bad ones.

> Premature optimization is the root of all evil (or at least most of it) in programming.
>
> --- Donald Knuth ---

In Python programming language, one can use `cProfile` module to profile a program to know where the bottleneck is. You can either export the profiled result to a file or have it printed directly in the terminal. The two options are shown below.
```sh
python -m cProfile -o result.pstats hello.py
python -m cProfile hello.py
```

However, sometimes what `cProfile` shows can be confusing (to me).
```txt
ncalls  tottime  percall  cumtime  percall filename:lineno(function)
1127/1    0.007    0.000    8.355    8.355 {built-in method builtins.exec}
     1    0.000    0.000    8.355    8.355 <string>:1(<module>)
     1    0.000    0.000    7.388    7.388 /home/quanhoang/hello.py:1(func)
...
```

That's where some visualization tools come into play. There are two available tools for this task: `gprof2dot` and `snakeviz`.

#### Gprof2doz


Installing required packages for [`gprof2dot`](https://github.com/jrfonseca/gprof2dot).
```sh
sudo apt install graphviz
pip install gprof2dot
```

One can create a graph of execution time either in `png` or `pdf` file format, then preview them by appropriate software programs.
```sh
gprof2dot -f pstats result.pstats | dot -Tpng -o result.png
eog result.png

gprof2dot -f pstats result.pstats | dot -Tpdf -o result.pdf
evince result.pdf
```


#### Snakeviz

Snakeviz, which can be installed via pip, is a browser-based visualization tool. Its usage is shown as follows:
```
pip install snakeviz --user
snakeviz result.pstats
```

#### References

[Narendra Kumar Vadapalli, Profiling and visualization tools in Python](https://medium.com/@narenandu/profiling-and-visualization-tools-in-python-89a46f578989)
