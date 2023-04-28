def POW(a, b, m):
    """繰り返し二乗法で計算
    使用例:abc156-d
    """
    ans = 1
    for i in range(100):
        if (b // 2**i) % 2 == 1:
            ans = (ans * a) % m
        a = (a * a) % m
    return ans


def DIV(a, b, m):
    """割り算をMODを取りながら計算
    使用例:abc156-d
    """
    return (a * POW(b, m - 2, m)) % m


# abc156-d
# n, a, b = map(int, input().split())
# MOD = 10**9 + 7
# ans = POW(2, n, MOD) - 1

# bunsi = [0] * (b + 1)
# bunsi[0] = 1

# bunbo = [0] * (b + 1)
# bunbo[0] = 1

# for i in range(b):
#     bunsi[i + 1] = (bunsi[i] * (n - i)) % MOD
#     bunbo[i + 1] = (bunbo[i] * (i + 1)) % MOD
# ans -= DIV(bunsi[a], bunbo[a], MOD)
# ans -= DIV(bunsi[b], bunbo[b], MOD)


# print(ans % MOD)
