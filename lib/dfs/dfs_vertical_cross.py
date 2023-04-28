"""縦十字の移動に限ったBFS
"""
# pypyではなく、Pythonじゃないと通らない
from collections import deque

import sys

sys.setrecursionlimit(10**6)


def dfs(pos):
    """深さ優先探索を行う関数
    posは現在位置、visited[x]は頂点xが青色かどうかを表す真偽値
    """
    x, y = pos
    if x < 0 or y < 0 or x >= H or y >= W:
        return
    if C[x][y] == "#":
        return
    # flatten_pos = H * x + y
    # print(H, x, y)
    if visited[x][y]:
        return
    visited[x][y] = True
    # print(visited)

    dfs((x + 1, y))
    dfs((x - 1, y))
    dfs((x, y + 1))
    dfs((x, y - 1))


H, W = map(int, input().split())
C = [list(input()) for _ in range(H)]

for h in range(H):
    for w in range(W):
        if C[h][w] == "s":
            s = (h, w)
        if C[h][w] == "g":
            g = (h, w)

# visited = [False] * (H * W)
visited = [[False] * W for _ in range(H)]
dfs(s)

# flatten_pos = H * g[0] + g[1]
if visited[g[0]][g[1]]:
    # if visited[flatten_pos]:
    print("Yes")
else:
    print("No")
