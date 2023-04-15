# 階差を考える
N, Q = map(int, input().split())
A = list(map(int, input().split()))
LRV = [list(map(int, input().split())) for i in range(Q)]

B = [0 for _ in range(N+1)]
ans = 0
for i in range(1, N):
    B[i] = A[i] - A[i-1]
    ans += abs(B[i])

for i in LRV:
    l, r, v = i
    mae = abs(B[l - 1]) + abs(B[r])
    if l > 1:
        B[l-1] += v
    if r < N:
        B[r] -= v

    ato = abs(B[l - 1]) + abs(B[r])
    ans += (ato - mae)
    print(ans)