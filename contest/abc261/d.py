N, M = map(int, input().split())
X = list(map(int, input().split()))
CY = [list(map(int, input().split())) for i in range(M)]

cy = [0]*(N+1)
for c, y in CY:
    cy[c] = y

dp = [[0]*(N+1) for i in range(N+1)]

for i in range(1,N+1):
    for j in range(1,i+1):
        dp[i][j] = dp[i-1][j-1] + X[i-1] + cy[j]

    dp[i][0] = max(dp[i - 1])

# for i in dp:
#     print(i)

print(max(dp[-1]))