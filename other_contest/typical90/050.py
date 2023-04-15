N, L = map(int, input().split())

dp = [1 for _ in range(L)]
for i in range(L, N+1):
    an = (dp[i-1] + dp[i-L]) % (10**9+7)
    dp.append(an)

print(dp[-1])