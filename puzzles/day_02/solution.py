with open('input.txt', 'r') as f:
    INPUT = f.read()


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


def p1():
    encrypted = {
        'X': 'r',
        'Y': 'p',
        'Z': 's',
    }

    score = 0

    for _round in ROUNDS:
        col1, col2 = _round.split(' ')
        opponent = OPPONENT[col1]
        protagonist = encrypted[col2]

        score += SCORES[protagonist]

        if opponent == protagonist:
            score += 3

        elif protagonist == 'r' and opponent == 's':
            score += 6

        elif protagonist == 's' and opponent == 'r':
            pass

        elif SCORES[protagonist] > SCORES[opponent]:
            score += 6

    return score


def p2():
    encrypted = {
        'X': 0,
        'Y': 3,
        'Z': 6,
    }

    score = 0

    for _round in ROUNDS:
        col1, col2 = _round.split(' ')
        opponent = OPPONENT[col1]
        result = encrypted[col2]

        score += result

        if result == 3:
            score += SCORES[opponent]

        elif result == 6:
            score += SCORES[opponent] % 3 + 1

        else:
            score += (SCORES[opponent] + 1) % 3 + 1

    return score


if __name__ == '__main__':
    print(p1(), p2())
