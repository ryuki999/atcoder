N, Q = map(int, input().split())
A = list(map(int, input().split()))
XY = [list(map(int, input().split())) for _ in range(Q)]

# 愚直実装(当然TLE)
# for i in range(Q):
#     x, y = XY[i]
#     p = list(range(N + 1))
#     for j in range(1, y + 1):
#         for k in range(N):
#             p[k + 1] = A[p[k + 1] - 1]
#     print(p)
#     print(p[x])

dp = [[0] * (N) for _ in range(30)]
# dp[0] = list(range(1, N + 1))
dp[0] = A

for i in range(29):
    for j in range(N):
        dp[i + 1][j] = dp[i][dp[i][j] - 1]
# for i in dp:
#     print(i)

for i in range(Q):
    x, y = XY[i]
    for j in reversed(range(30)):
        if (y // 2**j) % 2 != 0:
            x = dp[j][x - 1]
    print(x)
