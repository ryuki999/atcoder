N, K = map(int, input().split())
A = list(map(int, input().split()))

dp = [False] * (N+1)
for i in range(N+1):
    for j in range(K):
        if i >= A[j] and not dp[i-A[j]]:
            dp[i] = True

# print(dp)
if dp[N]:
    print("First")
else:
    print("Second")