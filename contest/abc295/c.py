import copy
from bisect import bisect_left
from collections import defaultdict

N = int(input())
A = list(map(int, input().split()))

d = defaultdict(int)
for i in range(N):
    d[A[i]] += 1

ans = 0
for i, v in d.items():
    ans += v // 2

print(ans)
