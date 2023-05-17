from collections import deque

N, Q = map(int, input().split())

G = [list() for _ in range(N + 1)]
for _ in range(N - 1):
    a, b = map(int, input().split())
    G[a].append(b)
    G[b].append(a)
# print(G)


q = deque()
q.append(1)
dist = [-1] * (N + 1)
dist[1] = 0

while len(q) > 0:
    pos = q.popleft()
    for to in G[pos]:
        if dist[to] == -1:
            dist[to] = dist[pos] + 1
            q.append(to)
            # print(dist)
for _ in range(Q):
    c, d = map(int, input().split())

    # print(dist[c], dist[d])
    if (dist[d] - dist[c]) % 2 == 0:
        print("Town")
    else:
        print("Road")
