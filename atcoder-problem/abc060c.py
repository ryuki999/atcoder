import sys

N, T = map(int, input().split())
t = list(map(int, input().split()))


sum_t = 0
for i in range(0, N-1):
    sum_t += min(t[i+1]-t[i], T)
    # print(sum_t)
sum_t += T
print(sum_t)