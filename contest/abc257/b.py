import copy
import sys

import numpy as np

N, K, Q = map(int, input().split())
A = list(map(int, input().split()))
L = list(map(int, input().split()))

for i in L:
    if A[i-1] + 1 not in A and (A[i-1] + 1) <= N:
        A[i-1] += 1

print(*A)