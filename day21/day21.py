import contextlib
import collections
import copy
import functools
import itertools
import numpy as np
import pandas as pd
import re
import matplotlib.pyplot as plt

import advent_tools


def convert_pattern_to_grid(pattern):
    lines = pattern.split('/')
    size = len(lines)
    grid = np.empty((size, size), dtype=int)
    char_map = {'.' : 0, '#' : 1}
    for y_pos, line in enumerate(lines):
        for x_pos, char in enumerate(line):
            grid[y_pos, x_pos] = char_map[char]
    return grid

def equivalent_grids(grid):
    result = [grid, grid.transpose(),
              np.flip(grid, axis=0), np.flip(grid, axis=0).transpose(),
              np.flip(grid, axis=1), np.flip(grid, axis=1).transpose(),
              np.flip(np.flip(grid, axis=0), axis=1),
              np.flip(np.flip(grid, axis=0), axis=1).transpose(),
              ]
    return result


def convert_grid_to_pattern(grid):
    result = ''
    for row in grid:
        for val in row:
            if val:
                result += '#'
            else:
                result += '.'
        result += '/'
    return result[:-1]


def split(array, nrows, ncols):
    """Split a matrix into sub-matrices."""
    # https://stackoverflow.com/questions/11105375/how-to-split-a-matrix-into-4-blocks-using-numpy
    r, h = array.shape
    return (array.reshape(h//nrows, nrows, -1, ncols)
                 .swapaxes(1, 2)
                 .reshape(-1, nrows, ncols))


def break_up_grid(grid):
    size = grid.shape[0]
    if size % 2 == 0:
        return split(grid, 2, 2)
    else:
        return split(grid, 3, 3)


def assemble_subgrids(subgrids):
    size = int(np.math.sqrt(len(subgrids)))
    rows = []
    for i in range(size):
        rows.append(np.concatenate(subgrids[size*i:size*(i+1)], 1))
    return np.concatenate(rows, 0)


def iterate_fractal(num_iterations=18):
    pattern_map = advent_tools.dict_from_input_file()
    init_pattern = '.#./..#/###'
    cur_grid = convert_pattern_to_grid(init_pattern)
    for _ in range(num_iterations):
        sub_grids = break_up_grid(cur_grid)
        new_subs = []
        for sub_grid in sub_grids:
            possible_grids = equivalent_grids(sub_grid)
            possible_patterns = [convert_grid_to_pattern(grid)
                                 for grid in possible_grids]
            for pattern in possible_patterns:
                if pattern in pattern_map:
                    new_pattern = pattern_map[pattern]
                    break
            new_subs.append(convert_pattern_to_grid(new_pattern))
        cur_grid = assemble_subgrids(new_subs)
        print(_)
        # plt.imshow(cur_grid)
        # plt.show()
    return cur_grid.sum().sum()


def run_part_1():
    return iterate_fractal(5)

def run_part_2():
    return iterate_fractal(18)


if __name__ == '__main__':
    print(run_part_1())
    print(run_part_2())