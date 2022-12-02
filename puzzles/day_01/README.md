# Day 1: Calorie Counting
## Part 1
The premise of this puzzle is to find the elf carrying the most calories, and to find how many calories that elf is carrying.
Below is a sample of the puzzle input.
```
1000
2000
3000

4000

5000
6000

7000
8000
9000

10000
```
Each elf is carrying some number of snacks that are some number of calories.
Each snack is seperated by a new line and each elf's inventory is seperated by two new lines.
```python
1000  # elf 1, snack 1
2000  # elf 1, snack 2
3000  # elf 1, snack 3; 6000 calories carried

4000  # elf 2, snack 1; 4000 calories carried

5000  # elf 3, snack 1
6000  # elf 3, snack 2; 1100 calories carried
...
```
My solution loops through each elf's inventory and sums the calories of each snack carried.
The value of the sum is saved in `most_calories` if it is greater than that value.
After every elf's inventory has been gone through, `most_calories` would be the value of the highest sum.
```python
def p1():
    most_calories = 0  # initialize variable
    for elf in INPUT.split('\n\n')[:-1]:  # loop through elf's inventories
        calories = sum(int(c) for c in elf.split('\n'))  # sum calories
        if calories > most_calories:
            most_calories = calories
    return most_calories
```
The reason for the `[:-1]` in `INPUT.split('\n\n')[:-1]` is to remove the newline at the end of the input. 
Could I have just pasted the input without that new line? Yes, but I didn't.
## Part 2
The premise of this puzzle is to find the top three elves carrying the most calories, and to find how many calories they are carrying in total.
Unlike the previous puzzle, I can't just loop through the inventories of the elves and save them in one value.
I *could* modify the loop to store three values, then sum that at the end, but that would require way too many comparisons than is worth writing.
My solution to this was to make a list of all the calories sums, sort it, then sum the top three.
```python
def p2():
    # this becomes a list of the sum of calories of each elf's inventory
    calories = [sum(int(c) for c in elf.split('\n')) for elf in INPUT.split('\n\n')[:-1]]
    calories.sort(reverse=True)  # sort descending order
    top_calories = sum(calories[:3])  # sum top three most calories
    return top_calories
```
The one-liner is a bit ugly, but I did it cause why not 🤷.
That line is equivalent to this:
```python
calories = []
for elf in INPUT.split('\n\n')[:-1]:
    _calories = 0
    for c in elf.split('\n'):
        _calories += int(c)
    calories.append(_calories)
```
