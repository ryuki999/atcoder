a, b = map(int, input().split())

MOD = 10**9+7
k = 64

# 23(10111)なので、bを2**iで割った余が1のものだけ乗算する
ans = 1
for i in range(k):
    if (b // 2**i) % 2 == 1:
        ans = (ans * a) % MOD
    
    a = (a*a) % MOD
print(ans)
# print(a, b)