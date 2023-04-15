N, K = map(int, input().split())

for i in reversed(range(300)):
    if K**i <= N:
        N = N - K**i
        break
# print(N)
print(i + 1)
