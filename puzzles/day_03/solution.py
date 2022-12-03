with open('input.txt', 'r') as f:
    INPUT = f.read()


RUCKSACKS = INPUT.split('\n')[:-1]
PRIORITIES = ' abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'


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


def p2():
    priorities_sum = 0

    groups = [RUCKSACKS[i:i + 3] for i in range(0, len(RUCKSACKS), 3)]
    for group in groups:
        for item in group[0]:
            if item in group[1] and item in group[2]:
                priorities_sum += PRIORITIES.index(item)
                break

    return priorities_sum


if __name__ == '__main__':
    print(p1(), p2())
