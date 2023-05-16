N, K, Q = map(int, input().split())
A = list(map(int, input().split()))
L = list(map(int, input().split()))

h = [0] * K
for i in range(K):
    h[i] = A[i]

for l in L:
    if h[l - 1] == N:
        continue
    f = False
    for i in h:
        if h[l - 1] + 1 == i:
            f = True
            break
    if not f:
        h[l - 1] += 1
    # print(h)
print(*h)
