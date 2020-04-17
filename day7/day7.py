import advent_tools


def run_part_1():
    weights = {}
    children = {}
    for line in advent_tools.read_input_lines():
        if '->' in line:
            left, right = line.split('->')
            name, whole_weight = left.split()
            children[name] = right.replace(',', '').split()
        else:
            name, whole_weight = line.split()
            weight = int(whole_weight[1:-1])
        weights[name] = weight
    all_children = [item for lst in children.values() for item in lst]
    print(set(weights.keys()).difference(all_children))


def check_balance(weights, children, start_node):
    try:
        kids = children[start_node]
    except KeyError:
        return weights[start_node]
    child_weights = {child: check_balance(weights, children, child)
                     for child in kids}
    if min(child_weights.values()) != max(child_weights.values()):
        diff = (max(child_weights.values()) - min(child_weights.values()))
        for key, val in child_weights.items():
            new_weights = child_weights.copy()
            new_weights[key] = val + diff
            if min(new_weights.values()) == max(new_weights.values()):
                print(weights[key] + diff)
            new_weights = child_weights.copy()
            new_weights[key] = val - diff
            if min(new_weights.values()) == max(new_weights.values()):
                print(weights[key] - diff)
        return sum(child_weights.values()) + weights[start_node]
    return sum(child_weights.values()) + weights[start_node]


def run_part_2():
    weights = {}
    children = {}
    for line in advent_tools.read_input_lines():
        if '->' in line:
            left, right = line.split('->')
            name, whole_weight = left.split()
            children[name] = right.replace(',', '').split()
        else:
            name, whole_weight = line.split()
        weight = int(whole_weight[1:-1])
        weights[name] = weight
    check_balance(weights, children, 'dtacyn')


if __name__ == '__main__':
    # run_part_1()
    run_part_2()