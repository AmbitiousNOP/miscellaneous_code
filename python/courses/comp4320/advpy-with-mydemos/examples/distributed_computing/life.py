#!/usr/bin/env python


class Board:
    def __init__(self, size):
        self.data = [[False] * size for _ in range(size)]

    def tick(self):
        future = [x[:] for x in self.data]
        for x in range(len(self.data)):
            for y in range(len(self.data)):
                neighbors = self.count_neighbors(x, y)
                if neighbors < 2 or 4 < neighbors:
                    future[x][y] = False
                elif neighbors == 3:
                    future[x][y] = True
        self.data = future

    def count_neighbors(self, x, y):
        total = 0
        for dx in range(max(0, x-1), min(x+2, len(self.data))):
            for dy in range(max(0, y-1), min(y+2, len(self.data))):
                # Ignore the square itself
                if dx == x and dy == y:
                    continue

                total += 1 if self.data[dx][dy] else 0
        return total

    def __str__(self):
        return '\n'.join(
                ''.join(map(lambda y: '#' if y else '.', x))
                for x in self.data)
