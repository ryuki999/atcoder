N, M = map(int, input().split())
H = list(map(int,input().split()))
G = [ list() for i in range(N + 1) ]
for _ in range(M):
    A, B = map(int, input().split())
    G[A].append(H[B-1])
    G[B].append(H[A-1])

# print(G)

ans = 0
for i in range(N):
    g = G[i+1]
    m = H[i]
    idx = i
    for gi, j in enumerate(g):
        if m <= j:
            m = j
            idx = gi+1
    if idx == i:
        ans += 1

print(ans)