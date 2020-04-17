import pandas as pd


def run_part_1():
    result = pd.read_csv('input.txt', header=None, sep='\t')
    print((result.max(axis=1) - result.min(axis=1)).sum())


def run_part_2():
    result = pd.read_csv('input.txt', header=None, sep='\t')
    p = 0
    for ind, row in result.iterrows():
        for key, val in row.iteritems():
            row2 = row%val
            w = row2 == 0
            if sum(w) == 2:
                bignum = row[w].max()
                smallnum = row[w].min()
                p = p + bignum / smallnum
                break
    print(p)

if __name__ == '__main__':
    run_part_1()
    run_part_2()
