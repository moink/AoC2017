import advent_tools


def run_part_1():
    jumps = [int(line) for line in advent_tools.read_input_lines()]
    index = 0
    count = 0
    while True:
        try:
            new_jump = jumps[index]
            jumps[index] = new_jump + 1
            index = index + new_jump
        except IndexError:
            return count
        count = count + 1


def run_part_2():
    jumps = [int(line) for line in advent_tools.read_input_lines()]
    index = 0
    count = 0
    while True:
        try:
            new_jump = jumps[index]
            if new_jump >=3:
                jumps[index] = new_jump - 1
            else:
                jumps[index] = new_jump + 1
            index = index + new_jump
        except IndexError:
            return count
        count = count + 1


if __name__ == '__main__':
    print(run_part_1())
    print(run_part_2())