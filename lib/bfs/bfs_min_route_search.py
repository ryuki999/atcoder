"""グラフの最短経路探索&復元(一個前のノード表示)
ABC168d
"""
from collections import deque

N, M = map(int, input().split())
AB = [list(map(int, input().split())) for _ in range(M)]

G = [list() for _ in range(N + 1)]
for A, B in AB:
    G[A].append(B)
    G[B].append(A)

route = [list() for _ in range(N + 1)]

q = deque()
q.append(1)
dist = [-1] * (N + 1)
dist[1] = 0

while len(q) > 0:
    pos = q.popleft()
    for to in G[pos]:
        if dist[to] == -1:
            dist[to] = dist[pos] + 1
            route[to].append(pos)
            q.append(to)
        # print(dist)
# print(route)
# print(dist)
for i in dist[1:]:
    if i == -1:
        print("No")
        exit()
print("Yes")
for i in route[2:]:
    print(i[0])
