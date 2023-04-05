import sys

# 再帰呼び出しの深さの上限を 120000 に設定
sys.setrecursionlimit(10**6)

def dfs(pos, visited, x):
    """深さ優先探索を行う関数
    posは現在位置、visited[x]は頂点xが青色かどうかを表す真偽値
    """
    visited[pos] = True
    points[pos] += x
    # print(points)
    for i in G[pos]:
        if visited[i] == False:
            dfs(i, visited, x)

N, Q = map(int, input().split())
ab = [list(map(int, input().split())) for _ in range(N-1)]
px = [list(map(int, input().split())) for _ in range(Q)]

G = [list() for _ in range(N+1)]

for a, b in ab:
    G[a].append(b)
    # G[b].append(a)

# print(G)


points = [0] * (N+1)
for p, x in px:
    # dfs(p, x)
    visited = [False] * (N+1)
    dfs(p, visited, x)

print(*points[1:])

