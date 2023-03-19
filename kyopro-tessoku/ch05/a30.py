n, r = map(int, input().split())

MOD = 10**9+7

def POW(a, b, m):
    ans = 1
    for i in range(30):
        if (b // 2**i) % 2 == 1:
            ans = (ans * a) % m
        a = (a*a) % m
    return ans

def DIV(a, b, m):
    return (a * POW(b, m-2, m)) % m

t = 1
for i in range(1, n+1):
    t = (t * i) % MOD

div_t = 1
for i in range(1, r+1):
    div_t = (div_t * i) % MOD

for i in range(1, n-r+1):
    div_t = (div_t * i) % MOD

print(DIV(t, div_t, MOD))
