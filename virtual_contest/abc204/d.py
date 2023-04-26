"""肝
集合それぞれの総和の差が最小になるように二つの集合に分ける
全体総和(S)/2を越えたものの中で最小値が全体にかかる時間。
これは部分和問題で考えられる
"""
N = int(input())
A = list(map(int, input().split()))

W = 10**3 * 100 + 1
sumA = sum(A)

dp = [[False] * (sumA + 1) for _ in range(N + 1)]
dp[0][0] = True

for i in range(N):
    for j in range(sumA):
        if dp[i][j]:
            dp[i + 1][j] = True
            dp[i + 1][j + A[i]] = True

# for i in dp:
#     print(i)

for i in range(sumA):
    if dp[-1][i] and i > sumA // 2:
        print(i)
        break
