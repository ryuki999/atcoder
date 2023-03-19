N, A, B = map(int, input().split())

# dp = []
# if A > B:
#     lower = B
#     more = A
# else:
#     lower = A
#     more = B

# while len(dp) <= N:
#     for _ in range(lower):
#         dp.append(False)
#     for i in range(more):
#         dp.append(True)

dp = [False] * (N+1)

for i in range(N+1):
    if i >= A and not dp[i-A]:
        dp[i] = True
    elif i >= B and not dp[i-B]:
        dp[i] = True
    else:
        dp[i] = False

# print(dp)
if dp[N]:
    print("First")
else:
    print("Second")
