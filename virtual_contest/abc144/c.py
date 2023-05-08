from math import ceil


def divisor_enumeration(N):
    t = 10**26
    for i in range(1, ceil(N ** (1 / 2)) + 1):
        # print(i, b)
        j = N / i
        # print(i, j, N)
        if j.is_integer():
            if i + j < t:
                t = i + j
                ans = (i, j)
    return ans


N = int(input())

print(int(sum(divisor_enumeration(N))) - 2)
