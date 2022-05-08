---
title: "IP"
permalink: /ip/
layout: customPostLayout
date: 2022-03-21 02:00:00
last_modified_at: 2022-04-07
---

Integer programming (IP) is a powerful tool of solving problems, especially when tackling with combinatorics ones. As far as I know, all problems with finite search spaces can be translated into IP models. Even in the worst case, we can cut off each candidate once at a time until we find a feasible solution or prove the infeasibility of the problem. Besides the various uses in different scenario, IP models can be efficiently solved by [the fastest solver](https://www.gurobi.com/).

This page mainly contains my articles related to **Mixed-integer linear programming (MILP)**, a specific branch of IP. Hope that my adventure in integer programming would inspire you.

[Eight queens puzzle](/ip-adventure-part1-introduction/)

[List of (solvable) puzzle in krazydad.com](/list-of-solvable-puzzles-in-krazydad-dot-com/)

[Magic squares](/magic-squares/)

[Modelling problems using IP](/modelling-problems-using-IP/)


## Random thoughts

As [Bland's rules](https://en.wikipedia.org/wiki/Bland%27s_rule) stated:

> If the minimum ratio is shared by several rows, choose the row with the lowest-numbered column (variable) basic in it.

In the past, I applied the rules by choosing the row of constraint with the lowest-numbered index. It turns out to be wrong.
