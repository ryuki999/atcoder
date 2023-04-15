n, a, b = map(int, input().split())
MOD = 10**9 + 7


def POW(a, b, m):
    ans = 1
    for i in range(30):
        if (b // 2**i) % 2 == 1:
            ans = (ans * a) % m
        a = (a * a) % m
    return ans


def DIV(a, b, m):
    return (a * POW(b, m - 2, m)) % m


ans = POW(2, n, MOD) - 1

bunsi = [0] * (b + 1)
bunsi[0] = 1

bunbo = [0] * (b + 1)
bunbo[0] = 1

for i in range(b):
    bunsi[i + 1] = (bunsi[i] * (n - i)) % MOD
    bunbo[i + 1] = (bunbo[i] * (i + 1)) % MOD
ans -= DIV(bunsi[a], bunbo[a], MOD)
ans -= DIV(bunsi[b], bunbo[b], MOD)

# print(bunsi, bunbo)

print(ans % MOD)


# def comb(n, k):
#     if n < k:
#         return 0
#     x = 1
#     y = 1
#     for i in range(k):
#         x = x * (n - i) % MOD
#         y = y * (i + 1) % MOD
#     return x * POW(y, MOD - 2, MOD) % MOD


# ans = POW(2, n, MOD) - 1 - comb(n, a) - comb(n, b)
# print(comb(n, a), comb(n, b))
# print(ans % MOD)
