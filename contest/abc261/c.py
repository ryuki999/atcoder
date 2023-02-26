import copy
import sys
from collections import defaultdict
import numpy as np

# L1, R1, L2, R2 = map(int, input().split())
N = int(input())
# A = list(map(int, input().split()))
A = [i.strip() for i in sys.stdin.readlines()]


memory = defaultdict(int)

for i in range(N):
    if A[i] in memory:
        print(f"{A[i]}({memory[A[i]]})")
    else:
        print(A[i])
    memory[A[i]] += 1
