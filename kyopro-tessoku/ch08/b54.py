from collections import defaultdict

N = int(input())
A = [int(input()) for _ in range(N)]

d = defaultdict(int)
for i in range(N):
    d[A[i]] += 1

ans = 0
for i, v in d.items():
    ans += v * (v - 1) // 2

print(ans)
