---
title: "Tips and tricks in Python (part 2)"
date: 2021-11-19 21:30:00
last_modified_at: 2021-11-19
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

### More tricks to be appended ...
Hope you enjoyed the post. Please leave a comment if you have any useful tricks in Python to share with others.