import collections

import advent_tools


def read_data():
    data2 = advent_tools.dict_from_input_file('<->')
    data = {}
    for k, v in data2.items():
        data[int(k)] = [int(num) for num in v.split(',')]
    return data


def find_connected_set(connections, root_node):
    connected_set = {root_node}
    queue = collections.deque([root_node])
    while queue:
        node = queue.popleft()
        for newnode in connections[node]:
            if newnode not in connected_set:
                connected_set.add(newnode)
                queue.append(newnode)
    return connected_set


def run_part_1():
    data = read_data()
    connected_set = find_connected_set(data, 0)
    return(len(connected_set))


def run_part_2():
    data = read_data()
    count = 0
    unlinked = set(data.keys())
    while unlinked:
        count = count + 1
        root_node = unlinked.pop()
        connected_set = find_connected_set(data, root_node)
        unlinked = unlinked.difference(connected_set)
    return count


if __name__ == '__main__':
    print(run_part_1())
    print(run_part_2())