S = input()
T = input()

slen = len(S)
tlen = len(T)

dp = [[0]*(tlen+1) for _ in range(slen+1)]

for i in range(slen):
    for j in range(tlen):
        if S[i] == T[j]:
            dp[i+1][j+1] = max(dp[i][j]+1, dp[i+1][j], dp[i][j+1])
        else:
            dp[i+1][j+1] = max(dp[i+1][j], dp[i][j+1])

# for i in dp:
#     print(i)
    
print(dp[slen][tlen])