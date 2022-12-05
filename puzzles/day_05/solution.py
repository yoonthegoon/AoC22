import re


with open('input.txt', 'r') as f:
    INPUT = f.read()


CRATES = INPUT.split('\n\n')[0].split('\n')
INSTRUCTIONS = INPUT.split('\n\n')[1].split('\n')[:-1]


class Stack:
    def __init__(self, crates: list):
        self.crates = crates

    @property
    def top(self) -> str:
        return self.crates[-1]

    def move_to(self, moved_crates: list) -> None:
        self.crates += moved_crates

    def move_from(self, move_crates: int) -> list:
        moved_crates = reversed(self.crates[-move_crates:])
        self.crates = self.crates[:-move_crates]
        return list(moved_crates)

    def __repr__(self):
        return str(self.crates)


class CrateMover9000:
    def __init__(self, stacks: dict):
        self.stacks = {}
        for stack in stacks:
            self.stacks[stack] = Stack(stacks[stack])

    @property
    def top(self) -> str:
        tops = ''
        for stack in self.stacks.values():
            tops += stack.top
        return tops

    def follow_instruction(self, instruction: str) -> None:
        move_crates, from_stack, to_stack = (int(i) for i in re.findall(r'[0-9]+', instruction))
        self.stacks[to_stack].move_to(self.stacks[from_stack].move_from(move_crates))

    def __repr__(self):
        return str(self.stacks)


def make_stacks() -> dict:
    stacks = {}
    for i in range(1, len(CRATES[-1]), 4):
        stack = []
        for crate in reversed(CRATES[:-1]):
            if len(crate) > i:
                if re.match(r'[A-Z]', crate[i]):
                    stack.append(crate[i])
        stacks[int(CRATES[-1][i])] = stack
    return stacks


def p1():
    stacks = make_stacks()
    ship = CrateMover9000(stacks)
    for instruction in INSTRUCTIONS:
        ship.follow_instruction(instruction)
    return ship.top


def p2():
    class NewStack(Stack):
        def move_from(self, move_crates: int) -> list:
            moved_crates = self.crates[-move_crates:]
            self.crates = self.crates[:-move_crates]
            return moved_crates

    class CrateMover9001(CrateMover9000):
        def __init__(self, _stacks: dict):
            super().__init__(_stacks)
            self.stacks = {}
            for _stack in _stacks:
                self.stacks[_stack] = NewStack(_stacks[_stack])

    stacks = make_stacks()
    ship = CrateMover9001(stacks)
    for instruction in INSTRUCTIONS:
        ship.follow_instruction(instruction)
    return ship.top


if __name__ == '__main__':
    print(p1(), p2())
