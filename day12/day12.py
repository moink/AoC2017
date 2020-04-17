import contextlib
import collections
import copy
import functools
import itertools
import numpy as np
import pandas as pd
import re

import advent_tools


def run_part_1():
    data2 = advent_tools.dict_from_input_file('<->')
    data = {}
    for k, v in data2.items():
        data[int(k)] = [int(num) for num in v.split(',')]
    connected_set = {0}
    queue = collections.deque([0])
    while queue:
        node = queue.popleft()
        for newnode in data[node]:
            if newnode not in connected_set:
                connected_set.add(newnode)
                queue.append(newnode)
    return(len(connected_set))



def run_part_2():
    data2 = advent_tools.dict_from_input_file('<->')
    data = {}
    for k, v in data2.items():
        data[int(k)] = [int(num) for num in v.split(',')]
    count = 0
    unlinked = set(data.keys())
    while unlinked:
        count = count + 1
        root_node = unlinked.pop()
        connected_set = {root_node}
        queue = collections.deque([root_node])
        while queue:
            node = queue.popleft()
            for newnode in data[node]:
                if newnode not in connected_set:
                    connected_set.add(newnode)
                    queue.append(newnode)
        unlinked = unlinked.difference(connected_set)
    return count



if __name__ == '__main__':
    print(run_part_1())
    print(run_part_2())