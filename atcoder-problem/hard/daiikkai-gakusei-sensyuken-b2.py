N, K = map(int, input().split())
A = list(map(int, input().split()))

MOD = 10**9 + 7
# 愚直
tmpA = A * K
ans = 0
for i in range(N * K):
    for j in range(i, N * K):
        if tmpA[i] > tmpA[j]:
            ans += 1
print(tmpA, ans)

l = [0] * N
r = [0] * N
for i in range(N):
    for j in range(i + 1, N):
        if A[i] > A[j]:
            r[i] += 1
    for j in range(i):
        if A[i] > A[j]:
            l[i] += 1

print(A, l, r)


ans = 0
for i in range(N):
    # sum_l = sum(l) % MOD
    sum_K = (K * (K - 1) // 2) % MOD
    ans += (l[i] * sum_K) % MOD

    # sum_r = sum(r) % MOD
    sum_K = (K * (K + 1) // 2) % MOD
    ans += (r[i] * sum_K) % MOD

# print(sum_m, sum_K)
print(ans)
