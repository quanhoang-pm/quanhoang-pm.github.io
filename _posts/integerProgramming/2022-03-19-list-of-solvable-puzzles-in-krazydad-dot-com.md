---
title: "List of (solvable) puzzles in krazydad.com"
date: 2022-03-19 02:00:00
last_modified_at: 2022-10-12
categories:
  - mathematics
tags:
  - Python
---


Jim Bumgardners's [site](https://krazydad.com) is a really great resources of interesting puzzles. When I was a kid, I used to download a lot of puzzles here to entertain myself. At that time, my technique was purely reasoning and trial-and-error, there was no computer assistant.

As my life goes on, I realize that some of the puzzles are able to be solved by IP models. As of Mar 2022, I've selected a complete list of puzzles which can be solved by IP models and puzzles which can not. They are separated into some category by their types of IP models but the puzzles are NOT listed by difficulty.

One more thing is that I only consider a puzzle as if the input data (preferably text data, not an image) is understandable by the model. The part converting images to text data is not concerned here, though it can be challenging to do it correctly in some particular puzzles, e.g., Bridges.

### Easy puzzles
- Sudoku
- Raw-Sudoku-related variants: Jigsaw Sudoku, Samurai Sudoku, Hex Sudoku, X Sudoku, Killer Sudoku
- Jigoku, Futoshiki (unique-in-row/column conditions with comparisons)
- Binox (X/O game)
- Two Not Touch, Star Battle (fixed number of stars in each row/column)
- Haunted (counting clues to figure out ghosts/vampires/zombies)
- Suguru, Pixidoku
- Kakuro, Krypto Kakuro

### Medium puzzles (with hints)
- Skyscraper (introducing variables indicating comparison between buildings)
- Inkies (dealing with operators other than addition by forcing to choose one of pre-processing tuples)
- Sandwich Sudoku (using conditional constraints to specify terms of sums based on locations of 1s and 9s)
- Consecutive Sudoku (setting "or"-condition to model the not-white edges)

### Hard puzzles
Generally, they are as hard as TSP in the sense of cutting off disconnected components.
- Bridges (cutting of disconnected solutions by modeling number of bridges as indicators 0/1/2)
- Masyu (cutting off disconnected loops)
- Galaxies (cutting off disconnected shapes)
- Slitherlink (cutting off disconnected solutions)
- Battleship (cutting off adjacent solutions)

### Should-not-try-IP puzzles
- Mazes (it should be solved by BFS)
- Area 51 (connected components)
- Cow & Cactus (connected components)
- Ripple effect (no idea to model it efficiently)
- Cross Figures (dealing with operators other than addition)
- Krypto Inkies (the method handling Inkies does not work well here)


Hope I will find time to implement solvers for some kind of puzzles listed above. In the meantime, I'll be more than happy if you spend time making use of my ideas to write a program by yourself. Don't hesitate to let me know if you have anything to show.
