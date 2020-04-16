import advent_tools


def run_part_1():
    the_sum = 0
    data = [int(char) for char in advent_tools.read_whole_input()]
    print(sum(first for first, second in zip(data, data[1:] + [data[0]])
              if first==second))


def run_part_2():
    the_sum = 0
    data = [int(char) for char in advent_tools.read_whole_input()]
    jump = len(data) // 2
    print(sum(first for first, second in zip(data, data[jump:] + data[:jump]) if
              first == second))


if __name__ == '__main__':
    run_part_1()
    run_part_2()