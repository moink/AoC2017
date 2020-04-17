import contextlib
import collections
import copy
import functools
import itertools
import numpy as np
import pandas as pd
import re

import advent_tools

class Scanner(advent_tools.PlottingGrid):

    def __init__(self):
        super().__init__((20, 91))
        self.depth = {int(k): int(v) for k, v in
                  advent_tools.dict_from_input_file(':').items()}
        # super().__init__((5, 7))
        # self.depth = {0: 3, 1: 2, 4: 4, 6: 4}
        self.directions = {}
        self.positions = {}
        for k, v in self.depth.items():
            self.grid[0:v, k] = 1
            self.grid[0, k] = 2
            self.positions[k] = 0
            self.directions[k] = 1
        self.layer = 0

    def one_step(self):
        for k, pos in self.positions.items():
            dr = self.directions[k]
            new_pos = pos + dr
            self.grid[pos, k] = 1
            if self.grid[new_pos, k] == 0:
                self.directions[k] = - self.directions[k]
                new_pos = pos + self.directions[k]
            self.grid[new_pos, k] = 2
            self.positions[k] = new_pos
        self.layer = self.layer + 1
        caught = False
        if self.layer >=0:
            caught = self.grid[0, self.layer] == 2
            self.grid[0, self.layer] = 3
        # self.show()
        severity = 0
        # self.draw()
        if caught:
            severity = self.layer * self.depth[self.layer]
        #     self.show()
        return severity

    def many_steps(self, delay=0):
        self.layer = - delay
        caught = 0
        for steps in range(90 + delay):
            try:
                caught = caught + self.one_step()
            except IndexError:
                return(caught)
        return(caught)
        # self.show()

def run_part_1():
    p = Scanner()
    return(p.many_steps())
    # p.show()

def scanner_pos(depth, time):
    offset = time % ((depth - 1)* 2)
    if offset > depth - 1:
        return 2*(depth -1) - offset
    else:
        return offset

def run_part_2():
    depths = {int(k): int(v) for k, v in
             advent_tools.dict_from_input_file(':').items()}
    count = 1
    while True:
        if all(scanner_pos(depth, count + layer) != 0 for layer, depth in
               depths.items()):
           return count
        count = count + 1

if __name__ == '__main__':
    print(run_part_1())
    print(run_part_2())