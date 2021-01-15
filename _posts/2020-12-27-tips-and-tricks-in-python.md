---
title: "Tips and tricks in Python"
date: 2020-12-27 21:50:00
last_modified_at: 2021-01-15 11:50:00
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

### More tricks to be appended ...

Hope you enjoyed the post. Please leave a comment if you have any useful tricks in Python to share with others.
