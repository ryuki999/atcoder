from bisect import bisect, bisect_left, bisect_right
N = int(input())
A = list(map(int, input().split()))

# dp = [0] * (N+1)
# for i in range(N):
#     dp[i] = 1
#     for j in range(N):
#         if A[i] > A[j]:
#             dp[i] = max(dp[i], dp[j]+1)
#     print(dp)


# print(max(dp))

dp = [0] * (N+1)
L = []
LEN = 0

for i in range(N):
    pos = bisect_left(L, A[i])
    dp[i] = pos
    # 配列Lを更新
    if dp[i] >= LEN:
        L.append(A[i])
        LEN += 1
    else:
        L[dp[i]] = A[i]
    
    # print(dp, L)

print(LEN)