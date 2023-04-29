from collections import deque

N, M = map(int, input().split())

G = [list() for _ in range(N + 1)]

for i in range(M):
    A, B = map(int, input().split())
    G[A].append(B)

# print(G)

ans = 0
for i in range(1, N + 1):
    # print(i, "=====")
    visited = [False] * (N + 1)

    q = deque()
    q.append(i)
    while len(q) > 0:
        pos = q.popleft()
        visited[pos] = True
        for p in G[pos]:
            if not visited[p]:
                q.append(p)
    ans += sum(visited)
    # print(pos, p)
print(ans)
