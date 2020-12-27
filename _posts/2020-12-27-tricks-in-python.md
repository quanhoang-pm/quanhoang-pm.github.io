---
title: "Tricks in Python"
date: 2020-12-27 21:50:00
last_modified_at: 2020-12-27 21:50:00
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

### More tricks to be appended ...

Hope you enjoyed the post. Please leave a comment if you have any useful tricks in Python to share with others.
