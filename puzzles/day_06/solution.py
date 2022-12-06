with open('input.txt', 'r') as f:
    INPUT = f.read()


def start_of_marker(characters: int) -> int:
    marker = False
    for i, _ in enumerate(INPUT):
        signals = INPUT[i:i + characters]
        for signal in signals:
            if signals.count(signal) > 1:
                marker = False
                break
            marker = True
        if marker:
            return i + characters


def p1():
    return start_of_marker(4)


def p2():
    return start_of_marker(14)


if __name__ == '__main__':
    print(p1(), p2())
