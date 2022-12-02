# Day 2: Rock Paper Scissors
## Part 1
The premise of this puzzle is to find the total rock paper scissor score, assuming `X, Y, Z = rock, paper, scissor`.
Throwing rock, paper, or scissors give you 1, 2, or 3 points respectively.
You're also awareded 0, 3, or 6 points for losing, drawing, or winning the round.
Below is the sample input.
```
A Y
B X
C Z
```
For your opponent (the first column), `A, B, C = rock, paper, scissor`.
So we can reimagine the input to be like this:

| opponent | protagonist |
|----------|-------------|
| rock     | paper       |
| paper    | rock        |
| scissors | scissors    |
Here, I add a column to show how many points you earn from what you play and what the outcome is.

| opponent | protagonist | shape score | outcome score | total score |
|----------|-------------|-------------|---------------|-------------|
| rock     | paper       | 2           | 6             | 8           |
| paper    | rock        | 1           | 0             | 1           |
| scissors | scissors    | 3           | 3             | 6           |
`8 + 1 + 6 = 15`, so the total score and answer here would be 15.

In the start of my solution file, I define some constants to be used by both solve functions.
```python
OPPONENT = {
        'A': 'r',
        'B': 'p',
        'C': 's',
    }
SCORES = {
        'r': 1,
        'p': 2,
        's': 3,
    }

ROUNDS = INPUT.split('\n')[:-1]
```
If the `[:-1]` in `INPUT.split('\n\n')[:-1]` bothers you, good, that's the intent from now on 😊. 

My goal here is simple; add to the score the shape score of what the protagonist throws and add to the score the result of the round.
```python

def p1():
    encrypted = {
        'X': 'r',
        'Y': 'p',
        'Z': 's',
    }

    score = 0  # you start with no score before the first round

    for _round in ROUNDS:
        # this chunk gives us a value 'r', 'p', or 's' for the opponent or protagonist
        col1, col2 = _round.split(' ')
        opponent = OPPONENT[col1]
        protagonist = encrypted[col2]

        score += SCORES[protagonist]  # immediately i add to the score the value of the protagonist's shape

        # draw
        if opponent == protagonist:
            score += 3

        # special result cases
        elif protagonist == 'r' and opponent == 's':
            score += 6
        elif protagonist == 's' and opponent == 'r':
            pass

        # you've won if your shape's score is higher than the opponent's (after you've filtered out special cases
        elif SCORES[protagonist] > SCORES[opponent]:
            score += 6

        # lose
        else:
            pass

    return score
```
## Part 2
Turns out, `X, Y, Z = lose, draw, win`. The same score rules still apply.
taking the original sample input, we'd now expect a table like this:

| opponent | result | shape | outcome score | shape score | total score |
|----------|--------|-------|---------------|-------------|-------------|
| rock     | draw   | rock  | 3             | 1           | 4           |
| paper    | loss   | rock  | 0             | 1           | 1           |
| scissors | win    | rock  | 6             | 1           | 7           |
`4 + 1 + 7 = 12`, so the total score and answer here would be 12.
The only challenge here is determining which shape must be thrown to get the result we're meant to.
However, I just skip that entirely and go straight to adding to the score what the shape *should* score.
```python
def p2():
    encrypted = {
        'X': 0,
        'Y': 3,
        'Z': 6,
    }

    score = 0

    for _round in ROUNDS:
        col1, col2 = _round.split(' ')
        opponent = OPPONENT[col1]  # still 'r', 'p', or 's'
        result = encrypted[col2]  # either 0, 3, or 6

        score += result  # immediately i add to the score the result of the round

        if result == 3:
            score += SCORES[opponent]  # the protagonist's shape's score must be that of the opponent's in a draw

        # mod magic i explain later
        elif result == 6:
            score += SCORES[opponent] % 3 + 1
        else:
            score += (SCORES[opponent] + 1) % 3 + 1

    return score
```
So the modulos thingy is actually pretty neat.
I probably coulda done something similar in part 1, but it hadn't occured to me then.
However, it felt much more obvious here.
Let's look at the first use:
```python
elif result == 6:
    score += SCORES[opponent] % 3 + 1
```
We can break apart the steps I'm doing here in a simple table.

| opponent score | % 3 | + 1 |
|----------------|-----|-----|
| 1              | 1   | 2   |
| 2              | 2   | 3   |
| 3              | 0   | 1   |
With 1, 2, and 3 being representitive of rock, paper, and scissors respectively, we see that when 
the opponent throws rock, we throw paper, 
the opponent throws paper, we throw scissors,
and the opponent throws scissors, we throw rock.

In the case of the protagonist losing, it's a little more involved.

| opponent score | + 1 | % 3 | + 1 |
|----------------|-----|-----|-----|
| 1              | 2   | 2   | 3   |
| 2              | 3   | 0   | 1   |
| 3              | 4   | 1   | 2   |
Just the additional step of adding 1 to the score before modding value gets us exactly what we need to lose.
See if you can apply this method to part 1 (cause i don't feel like it 💅).