from collections import defaultdict

N = int(input())
A = list(map(int, input().split()))

d = defaultdict(int)
d = [0] * (100)
for i in range(N):
    d[A[i] % 100] += 1

ans = 0
for i in range(1, len(d) // 2):
    # print(i, j)
    ans += d[i] * d[100 - i]
ans += d[50] * (d[50] - 1) // 2
ans += d[0] * (d[0] - 1) // 2
print(ans)

# print(d)
