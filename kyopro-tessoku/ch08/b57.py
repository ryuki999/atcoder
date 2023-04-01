N, K = map(int, input().split())

dp = [[0] * (N + 1) for _ in range(5)]
# dp[0] = N - sum([int(i) for i in str(N)])

dp[0] = [j - sum(map(int, str(j))) for j in range(N + 1)]
# print(dp)

for i in range(4):
    for j in range(N + 1):
        dp[i + 1][j] = dp[i][dp[i][j]]

# for i in dp:
#     print(i)

for i in range(1, N):
    for j in reversed(range(5)):
        if (K // 2**j) % 2 != 0:
            i = dp[j][i]
    print(i)
