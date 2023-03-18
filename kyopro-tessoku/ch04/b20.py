"""
わからないから未AC
"""
S = input()
T = input()

slen = len(S)
tlen = len(T) 

MAX = 10**29
dp = [[MAX]*(tlen+1) for _ in range(slen+1)]

dp[0][0] = 0

for i in range(slen):
    for j in range(tlen):
        if i>=0 and j>=0 and S[i] == T[j]:
            dp[i+1][j+1] = min(dp[i][j], dp[i+1][j]+1, dp[i][j+1]+1)
        elif i>=0 and j>=0:
            dp[i+1][j+1] = min(dp[i+1][j]+1, dp[i][j+1]+1, dp[i][j]+1)
        # elif i>=0:
        #     dp[i+1][j+1] = dp[i][j+1]+1
        # elif j>=0:
        #     dp[i+1][j+1] = dp[i+1][j]+1

for i in dp:
    print(i)

print(dp[slen][tlen])