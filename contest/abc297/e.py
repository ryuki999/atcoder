N, K = map(int, input().split())
A = list(map(int, input().split()))

dp = [[0] *(N+1) for _ in range(K)]

for i in range(N):
    for j in range(K):
        dp[i] = A[i]