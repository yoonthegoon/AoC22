with open('input.txt', 'r') as f:
    INPUT = f.read()


class Tree:
    def __init__(self, height: int):
        self.height = height
        self.neighbors = {}

    def __repr__(self):
        n = self.neighbors.get('n')
        s = self.neighbors.get('s')
        e = self.neighbors.get('e')
        w = self.neighbors.get('w')

        n = n.height if n else '.'
        s = s.height if s else '.'
        e = e.height if e else '.'
        w = w.height if w else '.'

        return f'\n  {n}  \n {w}{self.height}{e} \n  {s}  \n'


class Forest:
    def __init__(self, grid: list[str]):
        self.grid = []
        for row in grid:
            self.grid.append([Tree(int(tree)) for tree in row])

        for i, row in enumerate(self.grid):
            for j, tree in enumerate(row):
                tree.neighbors['n'] = self.grid[i - 1][j] if i > 0 else None
                tree.neighbors['s'] = self.grid[i + 1][j] if i + 1 < len(self.grid) else None
                tree.neighbors['e'] = row[j + 1] if j + 1 < len(row) else None
                tree.neighbors['w'] = row[j - 1] if j > 0 else None

    @property
    def visible(self) -> int:
        def spam(trees: list[int], end: bool) -> bool:
            if end:
                index = len(trees) - 1
            else:
                index = 0

            tallest = max(trees)
            return trees.count(tallest) == 1 and index == trees.index(tallest)

        count = 0
        for i, row in enumerate(self.grid):
            for j, tree in enumerate(row):
                north = spam(
                    [t.height for t in [r[j] for r in self.grid[:i + 1]]],
                    True,
                )
                south = spam(
                    [t.height for t in [r[j] for r in self.grid[i:]]],
                    False,
                )
                east = spam(
                    [t.height for t in row[j:]],
                    False,
                )
                west = spam(
                    [t.height for t in row[:j + 1]],
                    True,
                )
                if north or south or east or west:
                    count += 1
        return count


def p1():
    forest = Forest(INPUT.split('\n'))
    return forest.visible


def p2():
    pass


if __name__ == '__main__':
    print(p1(), p2())
