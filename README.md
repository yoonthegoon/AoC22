# AoC22
[Advent of Code 2022](https://adventofcode.com/2022)
___
This is a repo to keep track of my submissions for Advent of Code 2022.  
I've decided to run a private leaderboard with friends for a bit of friendly competition.  
I'm going to be solving all that I can with the Python standard library.

Each day of puzzle is in this structure:
```
puzzles
├── day_01
│   ├── input.txt
│   ├── README.md
│   └── solution.py
:
└── day_25
    ├── input.txt
    ├── README.md
    └── solution.py
```
Each day has their puzzle input in `input.txt`, solutions in `solution.py`, and solutions' explanations in `README.md`.

Each day's `solution.py` will be structured something like:
```python
with open('input.txt') as f:
    INPUT = f.read()

def p1():  # part 1
    return 'answer'

def p2():  # part 2
    return 'answer'

if __name__ == '__main__':
    print(p1(), p2())
```
Each day's `README.md` will be structured something like:
> # Day N: Title
> ___
> ## Part 1
> ```python
> def p1():
>     return 'answer'
> ```
> Explanation.
> ## Part 2
> ```python
> def p2():
>     return 'answer'
> ```
> Explanation.