---
title: "Tips and tricks in Python"
date: 2020-12-27 21:50:00
last_modified_at: 2021-04-13 11:45:00
categories:
  - programming
tags:
  - Python
---

### Number formatting

I read two tricks about number formatting in a [Medium article](https://levelup.gitconnected.com/10-python-tips-for-better-code-1bbffde3b44d). The first trick is that underscores can be placed anywhere you prefer in a given number, but of course you should use them to separate the number the every three digits for better readability. The second one is a way to add commas in f-string literals. Here are how the tricks work.
```python
value = 12_34_5678_9
value = 123_456.789_789
print(f'{value:,}')
```

### Virtual environments in Python

See comparison between tools managing virtual environments in [a Realpython article](https://realpython.com/python-virtual-environments-a-primer/). Also see [a guide to create a virtual environments](https://packaging.python.org/guides/installing-using-pip-and-virtual-environments/).

```sh
# env is the name of the folder containing environment
python3 -m venv env
# activate the environment
source env/bin/activate

# install packages
pip install numpy
pip install numpy==1.18.4
pip install numpy>=1.0.0
pip install --upgrade numpy

# deactivate the environment
deactivate
```

[Instructions](https://docs.python-guide.org/dev/virtualenvs/) to install packages from a `requirements.txt` file.
```sh
pip freeze > requirements.txt
pip install -r requirements.txt
pip install -r PythonPackages.txt --upgrade;
```

### Accessing elements in a numpy array

Given a numpy array, one need to provide the value of element in a given coordinate.

```py
import numpy as np
# input
arr = np.array([
    [1, 2, 3],
    [4, 5, 6],
])
coor = (1, 2)
# output 6
```
A solution to this exercise is quite simple
```py
def getElement(arr, coor):
    x, y = coor
    return arr[x, y]
```
But what if the array dimension is not pre-provided? We then do not know the number of indices to unpack correctly in the line `x, y = coor`. In addition, the approach `return arr[*coor]` is not syntactically correct. Luckily, I have found out a workaround by using `item` method as follows
```py
def getElement2(arr, coor):
    # coor must be a tuple, not a list
    return arr.item(coor)
```

One last note is about the try/catch block. The IndexError error is raised when given indices are invalid (out of array's bounds). Negative indices may not be what you're dealing with, they are valid in numpy arrays though. Make sure that you know exactly what indices values you're passing to the method.

### Negative indices in numpy arrays

Given a 1-dimensional numpy array, suppose you want to extract the last _m_ elements of the array. The most naive approach would be
```py
import numpy as np
m = 2
arr = np.array([10, 20, 30, 40, 50])
print(arr[-m:])
```
However, when _m_ equals to 0, the code above returns the entire array instead of returns nothing as expected (... extract the last 0 elements ...). Of course if we know _m_ is a non negative number beforehand, we would have come up with something different or at least being aware of the approach's downsides. The lesson here is trying to identify as many edge cases as possible.

Back to our problem, the fix is relatively easy to find out
```py
length = arr.size
assert 0 <= m <= length
print(arr[length-m:])
```

### Coding without if statements

```py
def withIfStatement(bool_):
    if bool_:
        print('Hello')
    return None

def withoutIfStatements(bool_):
    for _ in filter(lambda x: bool_, [None]):
        print('Hello')
    return None

withIfStatement(True)
withoutIfStatements(True)
```

### More tricks to be appended ...

Hope you enjoyed the post. Please leave a comment if you have any useful tricks in Python to share with others.
