import copy
from collections import defaultdict
import math

# H, M = map(int, input().split())
N = int(input())
# T = input()
X = list(map(int, input().split()))
# AB = [list(map(int, input().split())) for i in range(M)]
# st = [list(map(int, input().split())) for i in range(Q)]

X.sort()

# print(X)
# print(X[N:])
# print(X[:-N])
# print(X[N:-N])
print(sum(X[N:-N]) / len(X[N:-N]))