def divisors(n):
    result = []
    i = 1
    while i * i <= n:
        if n % i == 0:
            result.append(i)
            if n // i != i:
                result.append(n // i)
        i += 1
    return result


def count_arithmetic_sequences(N):
    count = 0
    print(divisors(N))
    for divisor in divisors(N):
        n = divisor
        a1 = (N / n - n + 1) / 2
        print(a1)
        if N == n * (2 * a1 + n - 1):
            count += 1
    return count


N = int(input())
print(count_arithmetic_sequences(N))
