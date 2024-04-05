---
title: "IP"
permalink: /ip/
layout: customPostLayout
date: 2022-03-21 02:00:00
last_modified_at: 2024-04-05
---

Integer programming (IP) is a powerful tool of solving problems, especially when tackling with combinatorics ones. As far as I know, all problems with finite search spaces can be translated into IP models. Even in the worst case, we can cut off each candidate once at a time until we find a feasible solution or prove the infeasibility of the problem. Besides the various uses in different scenario, IP models can be efficiently solved by [Gurobi Optimizer - the fastest solver](https://www.gurobi.com/).

This page mainly contains my articles related to **mixed-integer linear programming (MILP)**, a specific branch of IP. Hope that my adventure in integer programming would inspire you.

[Eight queens puzzle](/mathematics/IP-adventure-eight-queen-puzzle/)

[Magic squares](/mathematics/IP-adventure-magic-squares/)

[List of (solvable) puzzle in krazydad.com](/mathematics/list-of-solvable-puzzles-in-krazydad-dot-com/)

[Modelling problems using IP](/mathematics/modelling-problems-using-IP/)


## Random thoughts

As [Bland's rules](https://en.wikipedia.org/wiki/Bland%27s_rule) stated:

> If the minimum ratio is shared by several rows, choose the row with the lowest-numbered column (variable) basic in it.

In the past, I applied the rules by choosing the row of constraint with the lowest-numbered index. It turns out to be wrong.

## Tips and tricks in Gurobi

```py
from gurobipy import GRB
import gurobipy as gp
import numpy as np

# (1) disable all output messages in Gurobi
customEnv = gp.Env(empty=True)
customEnv.setParam('OutputFlag', 0)
customEnv.start()
model = gp.Model('modelName', env=customEnv)

vars = model.addMVar(shape=(3, 4), vtype=GRB.BINARY)
# a b c d
# e f g h
# i j k l

# (2) sum by axis: axis=1 means horizontal summation
# (3) add vector-based constraints
model.addConstr(vars.sum(axis=1) == np.array([1, 3, 3])) # a+b+c+d=1, e+f+g+h=3, i+j+k+l=3

# (4) extract variables by custom indices
arrA = np.array([
    [0, 2],
    [1, 0],
    [2, 2],
])
model.addConstr(vars[arrA[:,0], arrA[:,1]].sum() == 2) # c+e+k=2
model.addConstr(vars[arrA[:,0], arrA[:,1]] == np.array([1, 0, 1])) # c=1, e=0, k=1

model.optimize()
print(vars.x)
```
