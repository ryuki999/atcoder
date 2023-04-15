MOD = 10**9 + 7


def comb(n, k):
    """MODを取りながら組み合わせを計算
    n, a, b = map(int, input().split())
    ans = pow(2, n, MOD) - 1 - comb(n, a) - comb(n, b)
    print(ans % MOD)
    """
    if n < k:
        return 0
    x = 1
    y = 1
    for i in range(k):
        x = x * (n - i) % MOD
        y = y * (i + 1) % MOD
    return x * pow(y, MOD - 2, MOD) % MOD
