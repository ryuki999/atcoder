from bisect import bisect_left, bisect_right

from math import isqrt, sqrt


def eratosthenes_sieve(n):
    primes = [True] * (n + 1)
    primes[0] = primes[1] = False
    for i in range(2, isqrt(n) + 1):
        if primes[i]:
            for j in range(i * i, n + 1, i):
                primes[j] = False
    return [p for p in range(2, n + 1) if primes[p]]


def count_combinations(N):
    N_sqrt = isqrt(N)
    N_sqrt2 = isqrt(N_sqrt)
    primes = eratosthenes_sieve(N_sqrt)
    # print(primes)
    # print(len(primes))
    answer = 0

    for a in primes:
        a_square = a * a

        min_b = a + 1
        max_b = isqrt(N // a_square)
        if a_square * min_b**2 > N:
            continue
        min_b_idx = bisect_left(primes, min_b)
        max_b_idx = bisect_right(primes, max_b)

        # print(a, min_b, max_b, min_b_idx, max_b_idx)

        for b_idx in range(min_b_idx, max_b_idx):
            b = primes[b_idx]

            # for b in primes:
            if a >= b:
                continue
            ab = a_square * b
            if ab >= N:
                break

            min_c = b + 1
            max_c = isqrt(N // ab)
            if ab * min_c**2 > N:
                continue
            min_c_idx = bisect_left(primes, min_c)
            max_c_idx = bisect_right(primes, max_c)

            # print(a, b, min_c, max_c, min_c_idx, max_c_idx)

            answer += max_c_idx - min_c_idx

    return answer


N = int(input())

print(count_combinations(N))
