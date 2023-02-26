import copy
import sys

import numpy as np

N, Q = map(int, list(input().split()))
S = input()

query = [list(map(int, i.strip().split())) for i in sys.stdin.readlines()]

num = 0
for i in range(Q):
    if query[i][0] == 1:
        num += query[i][1]

    elif query[i][0] == 2:
        a = query[i][1]-1 - (num % N)
        print(S[a])
    # print(query[i][0],query[i][1], S)
    

# print(max(a))