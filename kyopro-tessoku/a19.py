N, W = map(int, input().split())

WV = [list(map(int, input().split())) for _ in range(N)]

dp = [[0]*(W+1) for _ in range(N+1)]

for i in range(N):
    for j in range(W+1):
        if j < WV[i][0]:
            dp[i+1][j] = dp[i][j]
        
        if j >= WV[i][0]:
            dp[i+1][j] = max(dp[i][j-WV[i][0]]+WV[i][1], dp[i][j])

# for d in dp:
#     print(d)

print(dp[N][W])