from collections import deque

N, X, Y = map(int, input().split())

G = [list() for i in range(N + 1)]

for i in range(1, N):
    G[i].append(i + 1)
    G[i + 1].append(i)

G[X].append(Y)
G[Y].append(X)

# print(G)
c = [0] * (N + 1)
for i in range(1, N + 1):
    dist = [-1] * (N + 1)
    q = deque()
    q.append(i)
    dist[i] = 0
    while len(q) >= 1:
        pos = q.popleft()
        for to in G[pos]:
            if dist[to] == -1:
                dist[to] = dist[pos] + 1
                q.append(to)
    for j in range(i + 1, N + 1):
        k = abs(dist[i] - dist[j])
        c[k] += 1
        # print(len(q))
    # print(dist, c)

for i in range(1, N):
    print(c[i])
# print(c)
