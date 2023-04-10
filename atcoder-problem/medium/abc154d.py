N, K = map(int, input().split())
P = list(map(int, input().split()))

for i in range(N):
    P[i] = (P[i] * (P[i] + 1) / 2) / P[i]
# print(P)

pp = [0] * N
pp[0] = sum([P[i] for i in range(K)])
for i in range(1, N - K + 1):
    pp[i] = pp[i - 1] - P[i - 1] + P[i + K - 1]
    # print(pp)
print(max(pp))
