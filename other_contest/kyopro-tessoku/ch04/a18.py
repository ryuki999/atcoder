N, S = map(int, input().split())

A = list(map(int, input().split()))

dp = [[False]*(S+1) for _ in range(N+1)]

dp[0][0] = True

# print(dp)
for i in range(N):
    for j in range(S+1):
        # print(j+A[j])
        if j < A[i]:
            dp[i+1][j] = dp[i][j]

        if j >= A[i]:
            if dp[i][j-A[i]] or dp[i][j]:
                dp[i+1][j] = True

# for d in dp:
#     print(d)

# print(dp[N][S])

if dp[N][S]:
    print("Yes")
else:
    print("No")