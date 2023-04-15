"""ダブリング
"""
from copy import copy

S = input()
N = len(S)

# init = [1] * (N)
# for _ in range(10**5):
#     pre_init = copy(init)
#     for i in range(N):
#         if init[i] > 0 and S[i] == "R":
#             init[i] -= pre_init[i]
#             init[i + 1] += pre_init[i]
#         if init[i] > 0 and S[i] == "L":
#             init[i] -= pre_init[i]
#             init[i - 1] += pre_init[i]
#     # print(init, pre_init)
# print(*init)

dp = [[0] * (N) for _ in range(30)]

for i in range(N):
    if S[i] == "R":
        dp[0][i] = i + 1
    if S[i] == "L":
        dp[0][i] = i - 1

for i in range(29):
    for j in range(N):
        dp[i + 1][j] = dp[i][dp[i][j]]

ans = [0] * N
# for i in dp:
#     print(i)

for i in dp[-1]:
    ans[i] += 1
print(*ans)
