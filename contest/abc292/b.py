import copy
import math
from collections import defaultdict

N, Q = map(int, input().split())
# N = int(input())
# T = input()
# X = list(map(int, input().split()))
AB = [list(map(int, input().split())) for i in range(Q)]
# st = [list(map(int, input().split())) for i in range(Q)]

d = defaultdict(int)


for a, b in AB:
    if a == 1:
        d[b] += 1
    if a == 2:
        d[b] += 2
    if a == 3:
        if d[b] >= 2:
            print("Yes")
        else:
            print("No")

# X.sort()

# print(X)
# print(X[N:])
# print(X[:-N])
# print(X[N:-N])
# print(sum(X[N:-N]) / len(X[N:-N]))