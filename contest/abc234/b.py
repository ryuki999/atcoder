import sys

import numpy as np

N = map(int, input())

inputs = sys.stdin.readlines()

array = []
for i in inputs:
    array.append(list(map(int, i.strip().split(" "))))

matrix = []
for idx_i, i in enumerate(array):
    m = []
    for idx_j, j in enumerate(array):
        if idx_i != idx_j:
            length = np.sqrt((i[0] - j[0])**2 + (i[1] - j[1])**2)
            m.append(length)
        else:
            m.append(0)
    matrix.append(m)

print(np.max(matrix))
