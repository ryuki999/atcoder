from collections import defaultdict
N = int(input())
A = list(map(int, input().split()))

memo = defaultdict(int)
for i in range(N):
    memo[A[i]] += 1

sum_t = 0
for i in range(N+1):
    sum_t += memo[i] * (memo[i] - 1) // 2

for i in range(N):
    tmp1 = memo[A[i]] * (memo[A[i]] - 1) // 2
    tmp2 = (memo[A[i]] - 1) * (memo[A[i]] - 2) // 2
    print(sum_t - tmp1 + tmp2)