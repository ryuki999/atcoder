N = int(input())
A = list(map(int, input().split()))

A = sorted(A, reverse=True)

dp = [0] * (N + 1)
print(sum(A[:-1]))
