import copy
from bisect import bisect_left
from collections import defaultdict

N, M = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

C = A + B

C.sort()
# print(C)

for i in range(N):
    pos = bisect_left(C, A[i])
    print(pos+1, end=" ")
    # print(C.index(A[i])+1, end=" ")
print()

for i in range(M):
    pos = bisect_left(C, B[i])
    print(pos+1, end=" ")
    # print(C.index(B[i])+1, end=" ")
print()