# ソートして二分探索木
import bisect

N = int(input())
A = list(map(int, input().split()))
Q = int(input())
B = [int(input()) for i in range(Q)]

A.sort()

for b in B:
    idx = bisect.bisect(A,b)
    # print(A[idx-1], A[idx])
    diff1, diff2 = 200000000000000, 200000000000000
    if idx < N:
        diff1 = abs(A[idx]- b)
    if idx > 0:
        diff2 = abs(A[idx-1]-b)
    res = min(diff1, diff2)
    print(res)
