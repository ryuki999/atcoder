H, W = map(int, input().split())

MOD = 1000000007

def POW(a, b, m):
    ans = 1
    for i in range(30):
        if (b // 2**i) % 2 == 1:
            ans = ans * a % MOD
        a = a*a % MOD
    return ans

def DIV(a, b, m):
    return a * POW(b, m-2, m) % MOD

# H+W-2 C H-1
t = 1
for i in range(1, H+W-2+1):
    t = t*i % MOD

div_t = 1
for i in range(1, H-1+1):
    div_t = div_t*i % MOD

for i in range(1, H+W-2-(H-1)+1):
    div_t = div_t*i % MOD

print(DIV(t, div_t, MOD))