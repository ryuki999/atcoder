from collections import defaultdict

N, M = map(int, input().split())
A = list(map(int, input().split()))

d = defaultdict(int)
for i in range(M):
    d[A[i]] += 1

for i in range(1, N + 1):
    print(M - d[i])
