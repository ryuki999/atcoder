N = int(input())
A = list(map(int, input().split()))

dp = [0] * (N+1)
for i in reversed(range(2, N+1)):
    dp[A[i-2]] +=  (dp[i] + 1)
#     print(dp)
# print(dp)


print(*dp[1:])