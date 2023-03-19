import sys

# 再帰呼び出しの深さの上限を 120000 に設定
sys.setrecursionlimit(10**6)

def dfs(pos):
    """深さ優先探索を行う関数
    posは現在位置、visited[x]は頂点xが青色かどうかを表す真偽値
    pathは1~Nまでの単純パス
    """
    path.append(pos)
    if pos == N:
        for x in path:
            print(x, end=" ")
        print()
        exit()

    visited[pos] = True
    for i in G[pos]:
        if not visited[i]:
            dfs(i)
    path.pop()

N, M = map(int, input().split())
AB = [list(map(int, input().split())) for _ in range(M)]

# d = [[0]*N for _ in range(N)]
G = [ list() for i in range(N + 1) ]

for A, B in AB:
    G[A].append(B)
    G[B].append(A)

visited = [False] * (N+1)
path = []

dfs(1)
