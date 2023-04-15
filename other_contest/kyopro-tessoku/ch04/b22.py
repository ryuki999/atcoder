N = int(input())

A = [0] * (N+1)
B = [0] * (N+1)
IN = list(map(int, input().split()))
for i in range(2, N+1):
    A[i] = IN[i-2]

IN = list(map(int, input().split()))
for i in range(3, N+1):
    B[i] = IN[i-3]

# A = list(map(int, input().split()))
# B = list(map(int, input().split()))

# print(A)
# print(B)

MIN = 10**20
dp = [MIN] * (N+1)
dp[1] = 0
for i in range(1, N):
    if i <= N-1:
        dp[i+1] = min(dp[i+1], dp[i]+A[i+1])
    if i <= N-2:
        dp[i+2] = min(dp[i+2], dp[i]+B[i+2])


# print(dp)
print(dp[N])