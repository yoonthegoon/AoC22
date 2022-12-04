# Day 4: Camp Cleanup
## Part 1
The premise of this puzzle is to find how many evles' ranges fully contain others' ranges.
The sample input and visual explanation [here](https://adventofcode.com/2022/day/4#part2) is done real well, so I won't rewrite it 💁‍♀️.

Le't stake a look at my global scope.
```python
PAIRS = INPUT.split('\n')[:-1]

def build_range(sections: str) -> range:
    start, stop = sections.split('-')
    start, stop = int(start), int(stop) + 1
    return range(start, stop)
```
Nothing special at all is going on with `PAIRS`.
My `build_range` function will be used later to turn a string like `'2-4'` into a range `range(2, 5)`.
The stop is 1 greater in the range vs the string because the string represents it inclusively while `range` is exclusive for stop.
Making an actual `range` is going to be more convenient for me later when I try to find if something's inside it.

Let's also come up with another function `in_range` that just determines if a range fully contains another (for now 😉).
Checking to see if every value in a range is in another range is really inefficient.
It would be much better to check *only* if the *ends* of one range are in another.
```python
def in_range(r1: range, r2: range) -> bool:
    if (r1[0] in r2 and r1[-1] in r2) or (r2[0] in r1 and r2[-1] in r1):
        return True
    return False
```
Let's break apart what's going on in my if statement.
Splitting it up at the `or` makes it easier to understand.
Here's the first part:
```python
r1[0] in r2 and r1[-1] in r2
```
This has value true when the first and last value of the first range are in the second.
The second does the same, but switching the roles of the two ranges.
So the total effect is that the `in_range` function returns true if either range fully contains the other.

Now that all the hard stuff is dealt with, we can actually take a look at my solution for part 1.
```python
def p1():
    # we already know what this does
    def in_range(r1: range, r2: range) -> bool:
        if (r1[0] in r2 and r1[-1] in r2) or (r2[0] in r1 and r2[-1] in r1):
            return True
        return False

    full_contains = 0

    for pair in PAIRS:
        elf1, elf2 = pair.split(',')
        # turning the ranges from the input into python range objects
        range1, range2 = build_range(elf1), build_range(elf2)

        if in_range(range1, range2):
            full_contains += 1

    return full_contains
```
I feel that the rest of the code is pretty self-explanatory, so I won't explain it.
Totally not cause I don't really know what to say about it 🤐.
## Part 2
I feel like this problem earns the title of ***Least Change Between Parts***.
The only thing that has to be done here is to find out how many ranges overlap or partially cover one another, rather than fully cover.
This requires the smallest change.

Looking back at my `in_range` function, I can rewrite it so that searching for the ranges go like this:
```python
r1[0] in r2 or r1[-1] in r2
```
Notice any difference?
The only thing that happened was I changed the `and` to an `or`.
This means rather than looking to see if both ends of the range are in the other, it only cares that an end is in the range of the other.
So here's part 2 gg no re 🥱:
```python
def p2():
    def in_range(r1: range, r2: range) -> bool:
        if (r1[0] in r2 or r1[-1] in r2) or (r2[0] in r1 or r2[-1] in r1):
            return True
        return False

    overlaps = 0

    for pair in PAIRS:
        elf1, elf2 = pair.split(',')
        range1, range2 = build_range(elf1), build_range(elf2)

        if in_range(range1, range2):
            overlaps += 1

    return overlaps
```