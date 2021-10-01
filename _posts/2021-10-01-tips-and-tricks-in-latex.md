---
title: "Tips and tricks in LaTeX"
date: 2021-10-01 15:30:00
last_modified_at: 2021-10-01 15:30:00
categories:
  - programming
tags:
  - LaTeX
---


### Compile all tex files in a given directory

[Reference](https://tex.stackexchange.com/questions/169176/compile-all-tex-files-within-a-folder-at-once)

```sh
# cd /path/to/folder/
for fileName in *.tex
do
  echo "Compile $fileName"
  # redirect output
  latexmk -pdf "$fileName" > /dev/null
  # "latexmk -pdf" is equivalent to pdflatex

  myString=$(printf "%80s")
  echo ${myString// /_}
done
```
