---
title: "Documentation in Python"
date: 2020-06-06 14:45:00
last_modified_at: 2020-06-06 14:45:00
categories:
  - programming
tags:
  - documentation
  - Python
---

This blog post is my summary of an article about [documenting python code](https://realpython.com/documenting-python-code/) in Real Python. I also append to the post some tools relating to documentation.

### Why you need to document your code

Perhaps sometimes you find yourself in the situation when you're not sure about how _your_ code works. All you have is just lines of code without proper comments/docstrings.

As Guido van Rossum rightly said,
> "Code is more often read than written."

### Basics of Commenting Code
A simple way to document your code is to write comments. According to [PEP8](https://www.python.org/dev/peps/pep-0008/), comments should have 72 characters at most. It is used for some purposes as follows:
- Planning and Reviewing
```py
# first step, load the dataset
# second step, obtain desired values from the dataset
# etc
```
- Tagging
```py
# URGENT: fix security bugs
# TODO: implement a new feature
# TEMP: add a magic number to the result
```

Type hinting is an alternative way to explain your code. Keep in mind that type hinting is only available from Python 3.5+ (sorry 2.x users). The code snippet below describes an example.
```py
def getRandomNumber(seed: int) -> int:
    return 42
```

### Documenting Code Base with Docstrings
Below is an (useless) example of a single-lined docstring in a method.
```py
def foo():
    """A function doing nothing."""
    pass
```
Moreover, multi-lined docstrings are used to provide detailed explanation about the code. They have the following parts:
- A one-line summary line
- A blank line proceeding the summary
- Any further elaboration for the docstring

#### Three major categories of docstrings
Doctrings can be divided into three main categories (this part is copied from the article):
- Class Docstrings: Class and class methods
- Package and Module Docstrings: Package, modules, and functions
- Script Docstrings: Script and functions

Class docstrings should contain the following information:
- A brief summary of its purpose and behavior
- Any public methods, along with a brief description
- Any class properties (attributes)
- Anything related to the interface for subclassers, if the class is intended to be subclassed

Class method (as well as module functions) docstrings should contain the following:
- A brief description of what the method is and what it’s used for
- Any arguments (both required and optional) that are passed including keyword arguments
- Label any arguments that are considered optional or have a default value
- Any side effects that occur when executing the method
- Any exceptions that are raised
- Any restrictions on when the method can be called

Module docstrings should include the following:
- A brief description of the module and its purpose
- A list of any classes, exception, functions, and any other objects exported by the module

The script docstrings should be placed at the top of the script and describe the usage of the script.

#### Docstring Formats
The docstring styles of Numpy and Google are the two potential candidates for your choice. In my opinion, I prefer Numpy's style to Google's. Here are two examples of [Numpy's](https://sphinxcontrib-napoleon.readthedocs.io/en/latest/example_numpy.html
) and [Google's](https://sphinxcontrib-napoleon.readthedocs.io/en/latest/example_google.html
) styles. You can see the comparison between them [here](https://sphinxcontrib-napoleon.readthedocs.io/en/latest/#google-vs-numpy
).

In addition, here are [a guide to numpy/scipy documentation](https://numpy.org/doc/stable/docs/howto_document.html) and the [docstring](https://numpy.org/doc/stable/reference/generated/numpy.mean.html#numpy.mean
) of `numpy.mean` method.

### Documenting Your Python Projects
The section is about the layout of your projects. It mostly depends on the project's type (private, shared, or public one). Please refer to the original article for the information.

### Documentation Tools and Resources

[Pyment - manage several styles of docstrings](https://github.com/dadadel/pyment)

[Read the Docs](https://readthedocs.org/)

[The Hitchhiker’s Guide to Python!](https://docs.python-guide.org/)
