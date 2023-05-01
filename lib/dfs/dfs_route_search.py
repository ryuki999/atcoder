import sys

# 再帰呼び出しの深さの上限を 120000 に設定
sys.setrecursionlimit(10**6)


def dfs(pos, G, visited):
    """深さ優先探索を行う関数
    posは現在位置、visited[x]は頂点xが青色かどうかを表す真偽値
    """
    # print(pos)
    ans.append(pos)
    visited[pos] = True
    for i in G[pos]:
        if visited[i] == False:
            dfs(i, G, visited)
            # print(pos)
            ans.append(pos)


N = int(input())
AB = [list(map(int, input().split())) for _ in range(N - 1)]

# d = [[0]*N for _ in range(N)]
G = [list() for i in range(N + 1)]

# print(AB)
for A, B in AB:
    G[A].append(B)
    G[B].append(A)

for i in range(N + 1):
    G[i] = sorted(G[i])

# print(G)
visited = [False] * (N + 1)
ans = []
dfs(1, G, visited)

print(*ans)
