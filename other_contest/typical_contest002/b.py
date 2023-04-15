N, M, P = map(int, input().split())


def POW(a, b, m):
    """繰り返し二乗法で計算
    使用例:abc156-d
    """
    ans = 1
    for i in range(100):
        # n^22 = n^2*n^4*n^16
        if (b // 2**i) % 2 == 1:
            ans = (ans * a) % m
        a = (a * a) % m
    return ans


ans = POW(N, P, M)
print(ans % M)
