import copy
from bisect import bisect, bisect_left, bisect_right
from collections import defaultdict

N, X = map(int, input().split())
A = list(map(int, input().split()))


ax = [0] * N
for i in range(N):
    ax[i] = A[i]-X

# print(ax)

A = sorted(A)

for i in range(N):
    pos = bisect_left(A,ax[i])
    # print(ax[i], A[pos], pos)
    if pos < N and pos > -1:
        if A[pos] == ax[i]:
            print("Yes")
            exit()

print("No")
