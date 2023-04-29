"""肝
集合それぞれの総和の差が最小になるように二つの集合に分け、大きい方の集合の総和が答え。
このとき、1つ目のオーブンを使う時間は全体総和(S)/2以上になり、S/2以上の最小値が全体にかかる時間となる。
これは、A1,A2,A3...,ANからいくつか選んだ和で、S/2以上の最小値は何かという、部分和問題で考えられる
"""
N = int(input())
A = list(map(int, input().split()))

W = 10**3 * 100 + 1
sumA = sum(A)

dp = [[False] * (sumA + 1) for _ in range(N + 1)]
dp[0][0] = 0
# dp[0][0] = True

for i in range(N):
    for j in range(sumA):
        if type(dp[i][j]) == int and j + A[i] <= sumA:
            dp[i + 1][j] = dp[i][j]
            # dp[i + 1][j] = True
            # dp[i + 1][j + A[i]] = True
            dp[i + 1][j + A[i]] = j + A[i]

# for i in dp:
#     print(i)

for i in range(sumA + 1):
    if dp[-1][i] and i >= sumA / 2:
        print(i)
        break
