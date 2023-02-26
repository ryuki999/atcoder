import copy
import sys
from collections import defaultdict
# N, M, X, T, D = map(int, input().split())

S = input()
# A = [list(map(int, list(i.strip()))) for i in sys.stdin.readlines()]

a = defaultdict(int)

for i in S:
    a[i] += 1

for i, v in a.items():
    if v == 1:
        print(i)
        exit()

print(-1)