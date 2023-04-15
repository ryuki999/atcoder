D, N = map(int, input().split())
LRH = [list(map(int, input().split())) for _ in range(N)]

INF = 24
dp = [INF] * (D + 1)
for l, r, h in LRH:
    for i in range(l, r + 1):
        dp[i] = min(dp[i], h)

print(sum(dp[1:]))
