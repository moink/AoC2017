import advent_tools


def move_dir(x, y, direction):
    if direction == 'n':
        y = y - 2
    if direction == 's':
        y = y + 2
    if direction == 'nw':
        x = x - 1
        y = y - 1
    if direction == 'ne':
        x = x + 1
        y = y - 1
    if direction == 'sw':
        x = x - 1
        y = y + 1
    if direction == 'se':
        x = x + 1
        y = y + 1
    return x, y


def run_part_1():
    x = 0
    y = 0
    for line in advent_tools.read_whole_input().split(','):
        x, y = move_dir(x, y, line)
    return abs(x) + max(0, (abs(y)- abs(x))/2)


def run_part_2():
    x = 0
    y = 0
    max_steps = 813
    for line in advent_tools.read_whole_input().split(','):
        x, y = move_dir(x, y, line)
        num_steps = abs(x) + max(0, (abs(y)- abs(x))/2)
        if num_steps > max_steps:
            max_steps = num_steps
    return max_steps


if __name__ == '__main__':
    print(run_part_1())
    print(run_part_2())