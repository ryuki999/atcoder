from collections import deque

H, W = map(int, input().split())
S = [list(input()) for _ in range(H)]

starts = []
goals = []
for i in range(H):
    for j in range(W):
        if S[i][j] == ".":
            starts.append((i, j))
# print(starts)

ans = 0
for s in starts:
    visited = [[False] * W for _ in range(H)]
    dist = [[-1] * W for _ in range(H)]

    q = deque()
    q.append(s)
    dist[s[0]][s[1]] = 0

    while len(q) > 0:
        pos = q.popleft()
        visited[pos[0]][pos[1]] = True
        poses = [
            (pos[0] + 1, pos[1]),
            (pos[0], pos[1] + 1),
            (pos[0] - 1, pos[1]),
            (pos[0], pos[1] - 1),
        ]
        for p in poses:
            x, y = p
            if x < 0 or y < 0 or x >= H or y >= W:
                continue
            if dist[x][y] == -1 and S[x][y] != "#":
                dist[x][y] = dist[pos[0]][pos[1]] + 1
                visited[x][y] = True
                q.append(p)
        # print(q)

    # print(s)
    for i in dist:
        ans = max(ans, max(i))
    # for i in visited:
    #     print(i)
    # print(q)
    # print("No")
print(ans)
