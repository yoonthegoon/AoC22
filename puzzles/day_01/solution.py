with open('input.txt', 'r') as f:
    INPUT = f.read()


def p1():
    most_calories = 0
    for elf in INPUT.split('\n\n')[:-1]:
        calories = sum(int(c) for c in elf.split('\n'))
        if calories > most_calories:
            most_calories = calories
    return most_calories


def p2():
    calories = [sum(int(c) for c in elf.split('\n')) for elf in INPUT.split('\n\n')[:-1]]
    calories.sort(reverse=True)
    top_calories = sum(calories[:3])
    return top_calories


if __name__ == '__main__':
    print(p1(), p2())
