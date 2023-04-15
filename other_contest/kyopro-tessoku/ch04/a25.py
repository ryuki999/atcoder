H, W = map(int, input().split())
C = [list(input()) for _ in range(H)]

dp = [[0]*W for _ in range(H)]
dp[0][0] = 1

for i in range(H):
    for j in range(W):
        t = 0
        if (i,j) == (0,0):
            continue
        if j-1 >= 0:
            t += dp[i][j-1]
        if i-1 >= 0:
            t += dp[i-1][j]

        if C[i][j] == ".":
            dp[i][j] = t
        if C[i][j] == "#":
            dp[i][j] = 0

# print(dp)
# for i in dp:
#     print(i)

print(dp[H-1][W-1])