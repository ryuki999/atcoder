K, N = map(int, input().split())
A = list(map(int, input().split()))

dp = [0] * (N)
for i in range(N):
    if i + 1 >= N:
        dp[i] = abs(K - A[i]) + abs(0 - A[0])
    else:
        dp[i] = abs(A[i] - A[i + 1])

dp = sorted(dp)

ans = 0
for i in range(N - 1):
    ans += dp[i]
print(ans)
