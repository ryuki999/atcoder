N, M = map(int, input().split())
A = list(map(int, input().split()))

dp = [[-10 **20 for _ in range(N+1)] for _ in range(N+1)]
dp[0][0] = 0
dp[0][1] = -10 **20

for i in range(1, N+1):
    for j in range(0, N+1):
        if j == 0:
            dp[i][0] = 0
        elif j > i:
            dp[i][j] = -10 **20
        else:
            dp[i][j] = max(dp[i-1][j], dp[i-1][j-1] + j * A[i-1])

# for i in dp:
#     print(i)
print(dp[N][M])