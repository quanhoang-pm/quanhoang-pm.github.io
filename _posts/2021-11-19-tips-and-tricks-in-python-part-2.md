---
title: "Tips and tricks in Python (part 2)"
date: 2021-11-19 21:30:00
last_modified_at: 2022-05-09
categories:
  - programming
tags:
  - Python
---


### Read files
```py
# my old method
with open(path, 'r') as f:
    lines = [x.replace('\n', '') for x in f.readlines()]

# a better method
with open(path, 'r') as f:
    lines = f.read().splitlines()

# perhaps it's the best method
lines = open(path, 'r').read().splitlines()
```


### Pandas
A slow approach
```py
def extractDataMethod(series):
    dict_ = {
        'open': series.date.min(),
        'closed': series.date.max(),
    }
    return pd.Series(dict_)
resultDf = combinedDf.groupby(['itemcode', 'shopcode'], as_index = False).apply(extractDataMethod)
```

A faster approach
```
openDf = combinedDf.groupby(['itemcode', 'shopcode'])['date'].min()
closedDf = combinedDf.groupby(['itemcode', 'shopcode'])['date'].max()
openDf.name = 'open'
closedDf.name = 'closed'
resultDf = pd.concat([openDf, closedDf], axis = 1)
resultDf.reset_index(inplace = True)
```

### Read params
Suppose we have a line read from a given file with the following convention
> For each line, the key and the value are separated by a colon.

```txt
# data.txt
projectFolder:/path/to/project/
dataFolder:/path/to/data/
```
```py
with open('data.txt', 'r') as f:
    allLines = f.readlines()
    line = allLines[0]
```

The task is to convert then given line to a (key, value) pair for further processing. The straight-forward way to handle it would be
```py
line = line.replace('\n', '')
key, value = line.split(':')
```
I was happy with that approach until a Windows-user come by and report an error when using the program. His/her `data.txt` contains
```txt
dataFolder:C:/path/to/data/
```
Unsurprisingly, a path can contain colons, especially in Windows. It leads to the following implementation
```py
line = line.replace('\n', '')
firstIndexOfColon = line.find(':')
key = line[:firstIndexOfColon]
value = line[firstIndexOfColon + 1:]
```

### Type hints in Python
[References](https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html)

```py
from typing import Tuple, List

foo: List[int] = [1, 2, 3]
bar: Tuple[int, ...] = (1, 2, 3, 4)
ham: Tuple[int, float, str] = (1, 2.0, 'three')
# egg: Tuple[int] = (1, 2, 3, 4) # wrong

# Use Optional[] for values that could be None
qux: Optional[str] = None
qux: Optional[str] = 'None'
```


### Working with zip files in Python
[References](https://docs.python.org/3/library/zipfile.html)
```py
from zipfile import ZipFile

with ZipFile('/path/to/data.zip') as zipObj:
    zipObj.printdir()
    # zipObj.extractall()
    for fileObj in zipObj.infolist():
        print(fileObj, fileObj.filename)
    with zipObj.open('subPath/to/file.txt', 'r') as f:
        data = f.readlines()
```

### Sorting an numpy array by its column
[The question and solution](https://stackoverflow.com/questions/2828059/sorting-arrays-in-numpy-by-column). [A solution](https://stackoverflow.com/a/2828371/11037273) to sort by multiple columns.

```py
arr = array([
  [9, 2, 3],
  [4, 5, 6],
  [7, 0, 5],
])
arr[arr[:, 1].argsort()] # sort by the second column
```

### Extract single member in a set
[References](https://stackoverflow.com/questions/1619514/how-to-extract-the-member-from-single-member-set-in-python)
```py
mySet = {27}
(element, ) = mySet
element = next(iter(myset))
```

### Verify non-empty intersections
[References](https://stackoverflow.com/questions/3170055/test-if-lists-share-any-items-in-python)
```py
len(set(M) & set(L)) >= 1 # naive way
not M.isdisjoint(L) # it's better for (very) small list sizes
any(x in M for x in L) # better way, where len(L) < len(M)
```

### Itertools library
```py
itertools.product([1, 2], repeat = 3) # 8 elements
itertools.product([1, 2], [3, 4, 5]) # 6 elements
itertools.combinations([1, 2, 3, 4, 5], r = 3) # 10 elements
itertools.permutations([1, 2, 3, 4, 5], r = 3) # 60 elements
itertools.permutations([1, 2, 3, 4, 5]) # 120 elements
itertools.chain.from_iterable([[1, 2], [3, 4, 5]]) # iterator of [1, 2, 3, 4, 5]
```

### Environment variables
Export variables in a terminal
```sh
# export FOO=$PWD
export FOO=/path/to/folder/output
export FOO="/path/to/folder/out put" # use quotation marks if space characters are included
```

Make use of them inside a Python script
```py
import os
print(*os.environ.items(), sep = '\n')
value = os.environ.get('FOO') # string
```

### Latin characters

```py
lowerCaseCharacters = [chr(x) for x in range(ord('a'), ord('z') + 1)]
upperCaseCharacters = [chr(x) for x in range(ord('A'), ord('Z') + 1)]
allCharacters = lowerCaseCharacters + upperCaseCharacters
```

### Intersection among lists
```py
def intersectionAmongLists(list_):
    return set(list_[0]).intersection(*list_[1:])
```

### Number of combinations
```py
import math
math.comb(7, 2) # 21
math.comb(7, 8) # 0
```

### The complex way and the intuitive way

```py
# it took me one day to be able to write this code snippet
value = (True, False)
if all(value):
    pass
elif not any(value):
    pass
else:
    pass

# but it took me one year to know the code below is much clearer
value = (True, False)
if value == (True, True):
    pass
elif value == (False, False):
    pass
else:
    pass
```


### More tricks to be appended ...
Hope you enjoyed the post. Please leave a comment if you have any useful tricks in Python to share with others.
