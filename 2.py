from itertools import *

def f(x, y, w, z):
    return (x == (not y)) <= ((x and w) == z)

for a1, a2, a3, a4, a5 in product([0, 1], repeat = 5):
    table = [(1, 1, a1, a2), (1, 1, a3, 1), (a4, 1, 1, a5)]
    if len(table) == len(set(table)):
        for p in permutations('xywz'):
            if [f( **dict(zip(p, r))) for r in table] == [0, 0, 0]:
                print(p)


