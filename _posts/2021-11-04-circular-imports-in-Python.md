---
title: "Cyclic imports in Python: How to handle it?"
date: 2021-11-04
last_modified_at: 2021-11-04 23:45:00
categories:
  - programming
tags:
  - Python
---

Cyclic imports often appear when the design contains complex dependency. This article describe the cases it emerges and the way to fix it.

### Minimal working example of cyclic imports

The folder is structured as follows

```txt
/baseFolder/project/
  main.py
  moduleA.py
  moduleB.py
```

```py
# main.py
from project.moduleA import printValueBInModuleA
from project.moduleB import printValueAInModuleB
printValueBInModuleA()
printValueAInModuleB()

# moduleA.py
from .moduleB import valueB
def printValueBInModuleA():
    print(valueB)
valueA = 'A-value'

# moduleB.py
from .moduleA import valueA
def printValueAInModuleB():
    print(valueA)
valueB = 'B-value'
```

After executing the following commands, an ImportError occurred.
```sh
cd /path/to/baseFolder
python project/main.py
# ImportError: cannot import name 'valueA' from partially initialized module 'project.moduleA' (most likely due to a circular import)
```

### A method to handle cyclic imports

Basically, you must not _mention_ variables if they have not been used. So instead of `from .moduleA import valueA`, it should be `from . import moduleA`. When it comes to using a variable in this module, it just simply be `moduleA.valueA`. The code below as expected.

```py
# moduleA.py
from . import moduleB
def printValueBInModuleA():
    print(moduleB.valueB)
valueA = 'A-value'

# moduleB.py
from . import moduleA
def printValueAInModuleB():
    print(moduleA.valueA)
valueB = 'B-value'
```

The method above can be used for default values in method declaration. That means, instead of writing code like (1), you write code like (2).

```py
# (1)
def someMethodInA(inputValue=moduleB.valueB):
    pass

# (2)
def someMethodInA(inputValue=None):
    if inputValue is None:
        inputValue = moduleB.valueB
```

### A problem with type hint

The cyclic imports arise (again) when using type hint with classes from another module.

```py
# main.py
from project.moduleA import classA
from project.moduleB import classB

# moduleA.py
from . import moduleB
class classA:
    pass
def newMethodInA(newInputValue: moduleB.classB):
    pass

# moduleB.py
from . import moduleA
class classB:
    pass
def newMethodInB(newInputValue: moduleA.classA):
    pass
```

The code above produces an ImportError. How can we mimic the approach for method declaration? Or there is another way to overcome this obstacle?

According to the accepted answer in [this link](https://stackoverflow.com/questions/39740632/python-type-hinting-without-cyclic-imports), we can take advantage of [PEP 563](https://www.python.org/dev/peps/pep-0563/) to resolve this one with the line
```py
from __future__ import annotations
```
on top of both `moduleA.py` and `moduleB.py`. It works like a charm. As the author stated, and I quote
> The `from __future__ import annotations` import will make all type hints be string and skip evaluating them.
