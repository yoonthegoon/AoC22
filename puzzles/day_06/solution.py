import re


with open('input.txt', 'r') as f:
    INPUT = f.read()


def re_factory(characters: int) -> str:
    pattern = '(.)'
    for i in range(1, characters):
        group = "|".join([f'\\{i}' for i in range(1, i + 1)])
        pattern += f'((?!{group})\\w)'
    return pattern


def p1():
    return re.search(re_factory(4), INPUT).span()[1]


def p2():
    return re.search(re_factory(14), INPUT).span()[1]


if __name__ == '__main__':
    print(p1(), p2())
