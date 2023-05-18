from bisect import bisect_left

N = int(input())
H = list(map(int, input().split()))

LEN = 0
L = []
dp = [0] * (N + 1)

for i in range(N):
    pos = bisect_left(L, H[i])
    dp[i] = pos

    if dp[i] >= LEN:
        LEN += 1
        L.append(H[i])
    else:
        L[dp[i]] = H[i]
    print(pos, dp, L)
print(LEN)
