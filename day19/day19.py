import contextlib
import collections
import copy
import functools
import itertools
import numpy as np
import pandas as pd
import re

from string import ascii_uppercase

import advent_tools

UP = 0
RIGHT = 1
DOWN = 2
LEFT = 3

class MazeGrid(advent_tools.PlottingGrid):

    def __init__(self):
        super().__init__((201, 40601//201))
        self.char_map = {' ': 0, '|': 1, '-': 2, '+': 3}
        for num, letter in enumerate(ascii_uppercase, start=4):
            self.char_map[letter] = num
        self.read_input_file(self.char_map)
        self.ypos = 0
        self.xpos = int(np.where(self.grid[0, :]==1)[0][0])

    def follow(self):
        result = []
        direction = DOWN
        y_max, x_max = self.grid.shape
        step_count = 0
        while True:
            step_count += 1
            cur_char = self.grid[self.ypos, self.xpos]
            if cur_char == self.char_map['+']:
                direction = self.pick_direction(direction, x_max, y_max)
            else:
                if direction == DOWN:
                    self.ypos = self.ypos + 1
                elif direction == UP:
                    self.ypos = self.ypos - 1
                elif direction == RIGHT:
                    self.xpos = self.xpos + 1
                else:
                    self.xpos = self.xpos - 1
                if cur_char == self.char_map[' ']:
                    break
                if cur_char not in [self.char_map['|'], self.char_map['-']]:
                    result.append(cur_char)
        return self.convert_to_letters(result), step_count - 1

    def pick_direction(self, direction, x_max, y_max):
        try_directions = [direction, (direction + 1) % 4, (direction - 1) % 4]
        for new_dir in try_directions:
            if new_dir == DOWN:
                next_xpos = self.xpos
                next_ypos = self.ypos + 1
            elif new_dir == UP:
                next_xpos = self.xpos
                next_ypos = self.ypos - 1
            elif new_dir == LEFT:
                next_xpos = self.xpos - 1
                next_ypos = self.ypos
            else:
                next_xpos = self.xpos + 1
                next_ypos = self.ypos
            if (next_ypos < 0 or next_xpos < 0 or next_ypos > y_max - 1
                    or next_xpos > x_max - 1):
                continue
            next_char = self.grid[next_ypos, next_xpos]
            if next_char != self.char_map[' ']:
                self.xpos = next_xpos
                self.ypos = next_ypos
                direction = new_dir
                break
        return direction

    def convert_to_letters(self, numbers):
        reverse_map = {val: key for key, val in self.char_map.items()}
        letters = [reverse_map[num] for num in numbers]
        return ''.join(letters)


def run_both_parts():
    grid = MazeGrid()
    return grid.follow()


if __name__ == '__main__':
    print(run_both_parts())
