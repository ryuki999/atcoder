import copy
import sys

import numpy as np

N = int(input())
A = np.array(list(map(int, input().split())))

p = 0
m = np.array([])

for a in A:
    m = np.append(m, 0)
    if a == 1:
        m += 1
    elif a == 2:
        m += 2
    elif a == 3:
        m += 3
    elif a == 4:
        m += 4
    # print(m, m>3)
    if sum(m > 3) != 0:
        for i in range(np.sum(m > 3)):
            p += 1
            m = np.delete(m, 0)
print(p)
