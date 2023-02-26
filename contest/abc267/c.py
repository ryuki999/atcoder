import copy

N, M = map(int, input().split())
A = list(map(int, input().split()))

total = 0
m = 0
for i in range(M):
  m += A[i]
  total += A[i] * (i+1)

memo = [m]
max_n = copy.copy(total)
# print(total)

for i in range(M, N):
  total -= memo[i-M]
  total += A[i] * M
  max_n = max(max_n, total)
  memo.append(memo[i-M] - A[i-M] + A[i])
  # print(total, memo)

print(max_n)