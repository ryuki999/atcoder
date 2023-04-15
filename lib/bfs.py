# 普通にTLEになる/PythonよりもPypyの方が良い
from collections import deque

H, W = map(int, input().split())
# C = []
# for _ in range(H):
#     C += list(input())
C = [list(input()) for _ in range(H)]

for h in range(H):
    for w in range(W):
        flatten_pos = H * h + w
        if C[h][w] == "s":
            s = (h, w)
            break
# print(s, g)

visited = [[False] * W for _ in range(H)]

q = deque()
q.append(s)

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
        if C[x][y] == "#":
            continue
        if visited[x][y]:
            continue
        if C[x][y] == "g":
            print("Yes")
            exit()
        q.append(p)
    # for i in visited:
    #     print(i)
    # print(q)
print("No")
