from math import ceil


def divisor_enumeration(N):
    """約数列挙(和が最小となる様な組み合わせ)
    N = int(input())
    print(int(sum(divisor_enumeration(N))) - 2)
    """
    t = 10**26
    for i in range(1, ceil(N ** (1 / 2)) + 1):
        j = N / i
        if j.is_integer():
            if i + j < t:
                t = i + j
                ans = (i, j)
    return ans
