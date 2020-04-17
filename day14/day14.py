import contextlib
import collections
import functools
from operator import xor

import numpy as np

import advent_tools

def run_operations(lengths, result, current_pos=0, skip_size=0):
    for length in lengths:
        reslen = len(result)
        to_rev = []
        positions = []
        for r in range(length):
            pos = (current_pos + r) % reslen
            positions.append(pos)
            to_rev.append(result[pos])
        revd = list(reversed(to_rev))
        for pos, item in zip(positions, revd):
            result[pos] = item
        current_pos = current_pos + length + skip_size
        skip_size = skip_size + 1
    return result, current_pos, skip_size

def convert_ascii(chars):
    return [ord(char) for char in chars]

def knot_hash(data):
    lengths = convert_ascii(data) + [17, 31, 73, 47, 23]
    pos = 0
    skip = 0
    result = list(range(256))
    for i in range(64):
        result, pos, skip = run_operations(lengths, result, pos, skip)
    dense = []
    for chunk in advent_tools.chunk_iterable(result, 16):
        hexval = hex(functools.reduce(xor, chunk, 0))
        if len(hexval) == 4:
            dense.append(hexval[2:])
        else:
            dense.append('0' + hexval[2:])
    return ''.join(dense)

class KnotGrid(advent_tools.PlottingGrid):

    def __init__(self):
        super().__init__((128, 128))
        root = 'vbqugkhl'
        # root = 'flqrgnkx'
        for row in range(128):
            to_hash = root + '-' + str(row)
            hashed = knot_hash(to_hash)
            b = bin(int('0x' + hashed, 16))[2:].zfill(128)
            for i, char in enumerate(b):
                self.grid[row, i] = int(char)
        self.show()

    def count_sets(self):
        unlinked = set(tuple(p) for p in np.argwhere(self.grid != 0))
        count = 0
        while unlinked:
            count = count + 1
            root_node = unlinked.pop()
            connected_set = self.find_connected_set(root_node, count)
            unlinked = unlinked.difference(connected_set)
        self.grid = 1250 - self.grid
        self.grid[self.grid==1250] = 0
        self.show()
        return count

    def find_connected_set(self, root_node, count):
        self.grid[root_node] = count
        connected_set = {root_node}
        queue = collections.deque([root_node])
        while queue:
            node = queue.popleft()
            y, x = node
            connections = [(y, x+1), (y, x-1), (y+1, x), (y-1, x)]
            for new_node in connections:
                if all(num >= 0 for num in new_node):
                    with contextlib.suppress(IndexError):
                        if self.grid[new_node]:
                            if new_node not in connected_set:
                                connected_set.add(new_node)
                                self.grid[new_node] = count
                                queue.append(new_node)
        return connected_set


def run_part_1():
    grid = KnotGrid()
    return grid.sum()


def run_part_2():
    grid = KnotGrid()
    return grid.count_sets()


if __name__ == '__main__':
    print(run_part_1())
    print(run_part_2())