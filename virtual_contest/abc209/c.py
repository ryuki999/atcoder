N = int(input())
C = list(map(int, input().split()))

MOD = 10**9 + 7
C = sorted(C)
ans = 1
for i in range(N):
    ans *= C[i] - i
    ans %= MOD
print(ans % MOD)
