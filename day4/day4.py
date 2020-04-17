import itertools

import advent_tools


def validate_function(inp):
    words = inp.split()
    for i, word in enumerate(words):
        if word in words[i+1:]:
            return False
    return True

def validate_function2(inp):
    words = inp.split()
    for i, word in enumerate(words):
        letters = [char for char in word]
        for anagram in itertools.permutations(letters):
            new_word = ''.join(anagram)
            if new_word in words[i+1:]:
                return False
    return True


def run_part_1():
    print(advent_tools.count_times_true(validate_function))


def run_part_2():
    print(advent_tools.count_times_true(validate_function2))


if __name__ == '__main__':
    run_part_1()
    run_part_2()