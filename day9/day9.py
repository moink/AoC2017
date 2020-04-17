import advent_tools

def total_score(data):
    split = advent_tools.recursive_inside_outside(data, '{', '}')
    return score(0, split)

def score(num, data):
    result = num
    if isinstance(data, dict):
        result = result + sum(score(num + 1, item) for item in data['inside'])
    else:
        return num
    return result

def remove_garbage(data):
    inside, outside = advent_tools.get_inside_outside_brackets(data, '<', '>',
                                                               False)
    result = ''.join(outside)
    count = sum(len(item) for item in inside)
    return result, count

def clean_ex(data):
    while '!' in data:
        pos = data.index('!')
        data = data[:pos] + data[pos+2:]
    return data

def run_both_parts():
    data = advent_tools.read_whole_input()
    data = clean_ex(data)
    data, count = remove_garbage(data)
    print('Part 1:', total_score(data))
    print('Part 2:', count)

if __name__ == '__main__':
    run_both_parts()