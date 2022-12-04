with open('input.txt', 'r') as f:
    INPUT = f.read()


PAIRS = INPUT.split('\n')[:-1]


def build_range(sections: str) -> range:
    start, stop = sections.split('-')
    start, stop = int(start), int(stop) + 1
    return range(start, stop)


def p1():
    def in_range(r1: range, r2: range) -> bool:
        if (r1[0] in r2 and r1[-1] in r2) or (r2[0] in r1 and r2[-1] in r1):
            return True
        return False

    full_contains = 0

    for pair in PAIRS:
        elf1, elf2 = pair.split(',')
        range1, range2 = build_range(elf1), build_range(elf2)

        if in_range(range1, range2):
            full_contains += 1

    return full_contains


def p2():
    def in_range(r1: range, r2: range) -> bool:
        if (r1[0] in r2 or r1[-1] in r2) or (r2[0] in r1 or r2[-1] in r1):
            return True
        return False

    full_contains = 0

    for pair in PAIRS:
        elf1, elf2 = pair.split(',')
        range1, range2 = build_range(elf1), build_range(elf2)

        if in_range(range1, range2):
            full_contains += 1

    return full_contains


if __name__ == '__main__':
    print(p1(), p2())
