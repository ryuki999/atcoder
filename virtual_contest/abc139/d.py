"""累積和+二分探索(or尺取り法)
ABC130d
"""
from bisect import bisect_left
from collections import deque

N, K = map(int, input().split())
A = list(map(int, input().split()))

# 累積和+二分探索
d = [0] * (N + 1)

for i in range(N):
    d[i + 1] = d[i] + A[i]

ans = 0
for i in range(N + 1):
    pos = bisect_left(d, K + d[i])
    ans += N - (pos - 1)
    print(pos, K + d[i], ans, d)
print(ans)

# 累積和+尺取り法
