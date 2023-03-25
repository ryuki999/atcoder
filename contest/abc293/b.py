import copy
import math
from collections import defaultdict

H, W = map(int, input().split())
# N = int(input())
# T = input()
# X = list(map(int, input().split()))
A = [list(map(int, input().split())) for i in range(H)]
# st = [list(map(int, input().split())) for i in range(Q)]

ALPHA = list("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
# d = defaultdict(int)
for i in A:
    for j in i:
        if j == 0:
            print(".", end="")
        else:
            print(ALPHA[j-1], end="")
    print()

# for a, b in AB:
#     if a == 1:
#         d[b] += 1
#     if a == 2:
#         d[b] += 2
#     if a == 3:
#         if d[b] >= 2:
#             print("Yes")
#         else:
#             print("No")

# X.sort()

# print(X)
# print(X[N:])
# print(X[:-N])
# print(X[N:-N])
# print(sum(X[N:-N]) / len(X[N:-N]))