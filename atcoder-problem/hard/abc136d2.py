from copy import copy

# N, K = map(int, input().split())
S = input()

N = len(S)

dp = [[0] * (N) for _ in range(30)]

init = [1] * (N)
# for i in range(N):
#     if S[i] == "R":
#         init[i] -= 1
#         init[i + 1] += 1
#     if S[i] == "L":
#         init[i] -= 1
#         init[i - 1] += 1
# dp[0] = init

# for i in dp:
#     print(i)


for _ in range(10):
    pre_init = copy(init)
    for i in range(N):
        if init[i] > 0 and S[i] == "R":
            init[i] -= 1
            init[i + 1] += 1
        if init[i] > 0 and S[i] == "L":
            init[i] -= 1
            init[i - 1] += 1
        print(init)

    print(init)
    print()


# for i in range(29):
#     for j in range(N):
#         dp[i + 1][j] = dp[i][dp[i][j] - 1]
# # for i in dp:
# #     print(i)

# for i in range(Q):
#     x, y = XY[i]
#     for j in reversed(range(30)):
#         if (y // 2**j) % 2 != 0:
#             x = dp[j][x - 1]
#     print(x)
