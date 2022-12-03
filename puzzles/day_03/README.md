# Day 3: Rucksack Reorganization
## Part 1
The premise of this puzzle is to find which "item" is common between the two compartments of each rucksack and add 
their priorities.
An item is just a letter character, upper or lower.
A rucksack is a bunch of items together on the same line.
A rucksack is also split up into two equal halves, both of those being a compartment.
Priorities of item go 1-26 for a-z and 27-52 for A-Z.

Let's start with my constants.
```python
RUCKSACKS = INPUT.split('\n')[:-1]
PRIORITIES = ' abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
```
The `RUCKSACKS` is pretty straightforward.
However, what the hell's going on with `PRIORITIES`?
The purpose of priorities being there is so that i can very easily get the priority of an item by doing 
`PRIORITIES.index(item)`.
The space in the beginning is to take up the 0 index, since no item has 0 priority.
I do gotta say though, it does feel silly typing the whole alphabet twice in one string 🤪.

Now let's look at my function.
```python
def p1():
    priorities_sum = 0

    for rucksack in RUCKSACKS:
        half = len(rucksack) // 2
        compartment1, compartment2 = rucksack[:half], rucksack[half:]
        for item in compartment1:
            if item in compartment2:
                priorities_sum += PRIORITIES.index(item)
                break

    return priorities_sum
```
You can see I use the `PRIORITIES.index(item)` I explained prior.
There's something else funky going on here.
`half = len(rucksack) // 2` gives me half of the length of the rucksack.
I use this to determine where I should slice the rucksack to produce the two compartments.
I can assign two values at once in `compartment1, compartment2 = rucksack[:half], rucksack[half:]`.
That's equivalent to `compartment1 = rucksack[:half]` followed by `compartment2 = rucksack[half:]`.
And the `[:half]` `[half:]` business is me slicing the rucksack up to the halfway point and me slicing from the 
halfway point onwards.
## Part 2
The premise here is that rather than figuring out which item is common among the two compartments of a rucksack, you've 
got to find out which item is common among a group of 3 rucksacks.

To do this, we need to be able to chunk a list into groups of 3.
This can be done with this cute oneline:
```python
groups = [RUCKSACKS[i:i + 3] for i in range(0, len(RUCKSACKS), 3)]
```
This is equivalent to the following:
```python
groups = []
for i in range(0, len(RUCKSACKS), 3):  # 0, 3, 6, ..., len(RUCKSACKS) - 1
    # same magic slicing from before, but we're only taking the element at the current index, along with the next two
    groups.append(RUCKSACKS[i:i + 3])
```
Don't tell anyone I searched in my work slack for this 🤫.

The next thing to figure out is how to find what item is common among each rucksack.
I do this by looping over each item in the first rucksack of a group then checking to see if it's in the other two rucksacks.
That sounds obvious in plain english but it may not be obvious to come up with. 
But when you read what I wrote, that's exactly what I did.
```python
def p2():
    priorities_sum = 0

    groups = [RUCKSACKS[i:i + 3] for i in range(0, len(RUCKSACKS), 3)]
    for group in groups:
        for item in group[0]:
            if item in group[1] and item in group[2]:
                priorities_sum += PRIORITIES.index(item)
                break

    return priorities_sum
```