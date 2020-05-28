import advent_tools


def run_part_1():
    ports = advent_tools.read_all_integers()
    cur_port = 0
    return score_part_1(cur_port, ports)


def score_part_1(cur_port, ports):
    poss_scores = [0]
    for consider in ports:
        if cur_port in consider:
            try:
                other_side = [pins for pins in consider if pins != cur_port][0]
            except IndexError:
                other_side = cur_port
            ports_left = [port for port in ports if port!=consider]
            poss_scores.append(cur_port + other_side
                               + score_part_1(other_side, ports_left))
    return max(poss_scores)

def score_part_2(cur_port, ports):
    poss_scores = [(0, 0)]
    for consider in ports:
        if cur_port in consider:
            try:
                other_side = [pins for pins in consider if pins != cur_port][0]
            except IndexError:
                other_side = cur_port
            ports_left = [port for port in ports if port!=consider]
            rest_length, rest_strength = score_part_2(other_side, ports_left)
            poss_scores.append((rest_length + 1,
                               rest_strength + cur_port + other_side))
    return max(poss_scores)


def run_part_2():
    ports = advent_tools.read_all_integers()
    cur_port = 0
    return score_part_2(cur_port, ports)


if __name__ == '__main__':
    print(run_part_1())
    print(run_part_2())