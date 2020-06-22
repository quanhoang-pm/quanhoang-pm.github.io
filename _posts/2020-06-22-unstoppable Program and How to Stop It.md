---
title: "An unstoppable script and how to stop it"
date: 2020-06-22
last_modified_at: 2020-06-22 23:40:00
categories:
  - programming
tags:
  - infinite
  - Python
  - terminal
---

In [a previous article](/the-shortest-infinite-program-in-Python/), we have constructed an infinite script in Python. That means the script does not simply stop itself once the execution has been begun. It brings us to a following question:

> Is it possible to (manually) stop an infinite script in Python?

The question above leads to another one.

> If it is possible, can we develop a script that is harder for users to terminate it?

In this blog post I'll show you what I have found while looking for the answer for these two questions.

### Stopping a script in Python

For the sake of simplicity, let's introduce a simple infinite script in Python as follows:
```py
# main.py
def infiniteLoop():
    while True:
        pass

infiniteLoop()
```
The script can be executed in terminal by the command `python3 main.py`. Obviously, the script won't stop itself. One can _easily_ terminate it by hitting the combination `Ctrl + C` and the generated traceback is shown below:
```sh
^CTraceback (most recent call last):
  File "main.py", line 6, in <module>
    infiniteLoop()
  File "main.py", line 4, in infiniteLoop
    pass
KeyboardInterrupt
```

Should we be self-satisfied with a way to terminate a script? Probably not.

### Developing an unstoppable script

One thing we can obtain from the traceback is that a `KeyboardInterrupt` error is raised to terminate the script [^other_note]. Therefore we can manage what to do if the error occurs by using a `try/except` block in the code. A naive attempt is to put another `infiniteLoop()` in the `except` block. It goes as follows:

[^other_note]: Another note is that `^C` stands for the combination `Ctrl + C`

```py
try:
    infiniteLoop()
except KeyboardInterrupt:
    infiniteLoop()
```

However, users still be able to terminate the script by hitting `Ctrl-C` *twice*. Of course we can handle the error raised when hitting `Ctrl-C` the second time.

```py
try:
    infiniteLoop()
except KeyboardInterrupt:
    try:
        infiniteLoop()
    except KeyboardInterrupt:
        infiniteLoop()
```
Sadly, hitting `Ctrl+C` _thrice_ is a way to stop the script above. We can append many `try/except` blocks to increase the complexity of the script but this approach is going nowhere since users can hitting `Ctrl+C` as many times as they prefer to stop the program.

### An idea and its implementation

What we really want is to make the script goes endlessly as follows:
```py
try:
    infiniteLoop()
except KeyboardInterrupt:
    try:
        infiniteLoop()
    except KeyboardInterrupt:
        try:
            infiniteLoop()
        except KeyboardInterrupt:
            ...
```
Our program must contain a finite number of characters, hence we can not naively implement the idea above. However, there is some kind of repetition here, it suggests us define a function to somehow shift the second `try` statement (at $4^\text{th}$ line) to the first `try` statement (at $1^\text{st}$ line). By some logical thinking, I can come up with the code below.
```py
def properInfiniteLoop():
    try:
        infiniteLoop()
    except KeyboardInterrupt:
        properInfiniteLoop()
```
Combining with all previous code snippets, we have the final version the the script. One can not stop the script by hitting `Ctrl + C`, no matter how many times the combination is used.
```py
# main.py
def infiniteLoop():
    while True:
        pass

def properInfiniteLoop():
    try:
        infiniteLoop()
    except KeyboardInterrupt:
        properInfiniteLoop()

properInfiniteLoop()
```

I was quite confident about my unstoppable script until I accidentally hit some keystrokes on keyboard ...

### Other methods to terminate a running script

While working on the this blog post, I accidentally hit the combination `Ctrl + \` [^atom_footnote] in terminal (in Ubuntu OS), the line `Quit (core dumped)` showed and the script stopped. In addition, it is not the only way to stop a process running in the system, `Ctrl + Z` combination and `kill` command are two alternative methods, just to name a few of them.

Perhaps there is no way to run a script endlessly without users' permission. It could be true, just for now.

[^atom_footnote]: I often use `Ctrl + \` to toggle the tree view while navigating in Atom to edit my script.
