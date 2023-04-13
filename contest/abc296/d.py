from math import ceil

N, M = map(int, input().split())

ans = 10**26
for i in range(1, ceil(M ** (1 / 2)) + 1):
    b = ceil(M / i)
    # print(i, b)
    if b > N:
        continue
    if i <= N and b <= N:
        ans = min(ans, b * i)
if ans == 10**26:
    ans = -1
print(ans)
