import copy
import sys

import numpy as np

N = int(input())
LR = sorted([list(map(int, i.strip().split())) for i in sys.stdin.readlines()])

ans = []

for i in LR:
    if len(ans) == 0:
        ans.append(i)
        continue
    elif not ans[-1][1] >= i[0]:
        ans.append(i)
        continue
    else:
        if i[0] <= ans[-1][1] and i[1] > ans[-1][1]:
            ans[-1][1] = i[1]

for i in ans:
    print(i[0], i[1])
