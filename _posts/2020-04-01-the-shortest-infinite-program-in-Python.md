---
title: "The shortest infinite program in Python"
date: 2020-04-01
last_modified_at: 2020-04-06 13:22:00
categories:
  - programming
tags:
  - infinite
  - shortest
---

Let's find out what it is and how it can be constructed.

## Program construction

Basically, infinite programs take an infinite amount of time to execute, i.e., they won't stop themselves during their execution.

A while loop allows us to execute a set of statements as long as a condition is satisfied. Keep that in mind, one can create an infinite loop (and thus an infinite program) by making sure that the condition is always true.

The implementation of this approach in Python programming language is shown as follows:

```py
x = 1
while x > 0:
    print('Hello World.')
```

## A shorter program
The code snippet above has a lot of characters (including space and new line ones). We can simplify it by two following actions:
- Using an always-true variable in the condition, that is `True`.
- Doing simple thing inside the `while` loop, for example, `x=1`.

The updated program is shown as follows:

```py
while True:
    x=1
```
Its 16 characters are `w h i l e 'space' T r u e : '\n' '\t' x = 1`.


## The shortest program (probably)

There are several conventions in Python to help us reduce the number of characters used in the program.

One convention is about a code snippet inside a while loop. It must not be empty, but it could do nothing at all. The `pass` keyword appears as a promising candidate but it has just one more character than `x=1`. Luckily, we can simply put `1` as the only statement and the code still does nothing.

```py
while True:
    1
```

Another convention is about variables (other than `True`) which can be evaluated as `True`. They are non-zero values or non-empty lists/tuples/sets. In our case, we can opt for the condition `while 1:` as a shorter one.

```py
while 1:
    1
```

Lastly, we need not to use indentation for a single-statement while loop. The statement can be written in the same line with the condition.

By applying these three conventions, we can syntactically shorten the infinite program to obtain the shortest infinite program with only 9 characters `w h i l e 'space' 1 : 1`. The program is shown as follows:

```py
while 1:1
```

## Last words
The article may have no effect on your daily workflow, even if you're a programmer. Who cares about programs that do not stop? Maybe someone who wants to break your laptop?

In the next article, I will present how I accidentally find out an unusual way to stop a program in Python.

Please let me know if you have any comments/suggestions.
