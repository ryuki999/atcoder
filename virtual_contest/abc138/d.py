import sys

# 再帰呼び出しの深さの上限を 120000 に設定
sys.setrecursionlimit(10**6)


def input():
    return sys.stdin.readline()[:-1]


N, Q = map(int, input().split())

G = [list() for _ in range(N)]
for _ in range(N - 1):
    a, b = map(int, input().split())
    G[a - 1].append(b - 1)
    G[b - 1].append(a - 1)

# ab = [list(map(int, input().split())) for _ in range(N - 1)]
# px = [list(map(int, input().split())) for _ in range(Q)]

points = [0] * N
for _ in range(Q):
    p, x = map(int, input().split())
    points[p - 1] += x

# print(G)

# visited = [False] * (N + 1)


# def dfs(pos, pre_pos, visited):
#     """深さ優先探索を行う関数
#     posは現在位置、visited[x]は頂点xが青色かどうかを表す真偽値
#     """
#     visited[pos] = True
#     if pos != pre_pos:
#         points[pos] += points[pre_pos]
#     for i in G[pos]:
#         if visited[i] == False:
#             dfs(i, pos, visited)


# dfs(1, 1, visited)


def dfs(pos, pre_pos):
    """深さ優先探索を行う関数
    posは現在位置、visited[x]は頂点xが青色かどうかを表す真偽値
    """
    for i in G[pos]:
        if i == pre_pos:
            continue
        points[i] += points[pos]
        dfs(i, pos)


dfs(0, 0)

# print(points)

print(*points)
