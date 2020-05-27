import contextlib
import collections
import copy
import functools
import itertools
import numpy as np
import pandas as pd
import re

import advent_tools


def take_one_step(particles):
    for part_num, part in enumerate(particles):
        for ind in [3, 4, 5, 0, 1, 2]:
            part[ind] += part[ind + 3]
        particles[part_num] = part


def run_part_1():
    particles = advent_tools.read_all_integers()
    result = []
    for _ in range(1000):
        take_one_step(particles)
        distances = [abs(part[0]) + abs(part[1]) + abs(part[2]) for part in
                     particles]
        result.append(np.argmin(distances))
    return result[-1]


def run_part_2():
    particles = advent_tools.read_all_integers()
    for _ in range(40):
        marked = set()
        for index1 in range(len(particles)):
            for index2 in range(index1 + 1, len(particles)):
                if particles[index1][:3] == particles[index2][:3]:
                    marked.add(index1)
                    marked.add(index2)
        particles = [part for index, part in enumerate(particles)
                     if index not in marked]
        take_one_step(particles)
    return len(particles)

if __name__ == '__main__':
    print(run_part_1())
    print(run_part_2())