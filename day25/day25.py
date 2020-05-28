import contextlib
import collections
import copy
import functools
import itertools
import numpy as np
import pandas as pd
import re

import advent_tools


class TuringMachine:

    def __init__(self):
        self.state = 'A'
        self.position = 0
        self.tape = collections.defaultdict(bool)
        program = advent_tools.read_whole_input()
        program = program + '\n\n'
        flags = re.MULTILINE | re.DOTALL
        state_pat = r'(In state ([A-Z]):.*?\n\n)'
        state_descs = re.findall(state_pat, program, flags)
        self.cases = {}
        cur_pat = re.compile(
            r'If the current value is ([0-1]):\n\s*'
            r'- Write the value ([0-1]).\n\s*'
            r'- Move one slot to the ([a-z]*).\n\s*'
            r'- Continue with state ([A-Z]).', flags)
        for subtext, state in state_descs:
            cur_descs = re.findall(cur_pat, subtext)
            for cur_val, write_val, direction, new_state in cur_descs:
                if direction == 'right':
                    increment = 1
                else:
                    increment = -1
                self.cases[(state, bool(int(cur_val)))] = (
                    bool(int(write_val)), increment, new_state)


    def take_one_step(self):
        to_do = self.cases[(self.state, self.tape[self.position])]
        self.do_stuff(*to_do)

    def run(self):
        for count in range(12656374):
            self.take_one_step()
            if count % 100000 == 0:
                print(count)
        return sum(self.tape.values())

    def do_stuff(self, to_write, to_move, new_state):
        self.tape[self.position] = to_write
        self.position = self.position + to_move
        self.state = new_state


def run_part_1():
    machine = TuringMachine()
    print(machine.cases)
    return machine.run()


def run_part_2():
    pass


if __name__ == '__main__':
    print(run_part_1())
    print(run_part_2())