import sys
from collections import deque

N, M = map(int, input().split())
AB = [list(map(int, input().split())) for _ in range(M)]

G = [ list() for i in range(N + 1) ]

# print(AB)
for A, B in AB:
    G[A].append(B)
    G[B].append(A)

dist = [-1] * (N+1)

q = deque()
q.append(1)
dist[1] = 0

# print(G)
# print(dist)
while len(q) >= 1:
    pos = q.popleft()
    for to in G[pos]:
        if dist[to] == -1:
            dist[to] = dist[pos] + 1
            q.append(to)
    # print(len(q))

for i in range(1, N+1):
    print(dist[i])


