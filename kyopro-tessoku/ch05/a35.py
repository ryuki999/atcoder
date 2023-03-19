N = int(input())
A = list(map(int, input().split()))

dp = [[0] * (N+1) for _ in range(N)]

for i in range(N):
    dp[N-1][i] = A[i]

# print(dp)

for i in reversed(range(1, N)):
    for j in range(i):
        if i % 2 == 1:
            dp[i-1][j] = max(dp[i][j], dp[i][j+1])
        else:
            dp[i-1][j] = min(dp[i][j], dp[i][j+1])

# for i in dp:
#     print(i)

print(dp[0][0])