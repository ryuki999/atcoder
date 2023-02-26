import copy
import sys
from queue import Queue

import numpy as np

N, M, K, S, T, X = input().split(" ")
U = [list(map(int, i.strip().split(" "))) for i in sys.stdin.readlines()]
print(U)

ans = 1
q = []
q.append(S)
while len(q) > 0:
    target = q.pop(0)
    count = 0
    for edge in U:
        if target == edge[0]:
            count += 1
            if edge[1] not in q:
                q.append(edge[1])
        elif target == edge[1]:
            count += 1
            if edge[0] not in q:
                q.append(edge[0])

    ans *= count
    print(q)

print(ans % 998244353)
