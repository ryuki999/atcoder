import math

N, X = map(int, input().split())
L = list(map(int, input().split()))

d = [0] * (N + 1)

for i in range(N):
    d[i + 1] = d[i] + L[i]

# print(d)

ans = 0
for i in range(len(d)):
    if d[i] <= X:
        ans += 1

print(ans)
