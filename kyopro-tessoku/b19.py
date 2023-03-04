N, W = map(int, input().split())

WV = [list(map(int, input().split())) for _ in range(N)]

V = 1000 * 100
# MAX = 0
MAX = 10**29
dp = [[MAX]*(V+1) for _ in range(N+1)]
dp[0][0] = 0

for i in range(N):
    for j in range(V+1):
        if j < WV[i][1]:
            dp[i+1][j] = dp[i][j]
        
        if j >= WV[i][1]:
            dp[i+1][j] = min(dp[i][j-WV[i][1]]+WV[i][0], dp[i][j])

# for d in dp:
#     print(d[:50])

l_m = 0
for i, v in enumerate(dp[N]):
    if v <= W:
        l_m = max(i, l_m)

print(l_m)
# print(min(dp[N]))