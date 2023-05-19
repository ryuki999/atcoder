"""DFSとスタックを使った単純パス探索
abc270c
"""
import sys
from collections import deque

# 再帰呼び出しの深さの上限を 120000 に設定
sys.setrecursionlimit(10**6)


N, X, Y = map(int, input().split())

G = [list() for _ in range(N + 1)]

for _ in range(N - 1):
    a, b = map(int, input().split())
    G[a].append(b)
    G[b].append(a)


def dfs(pos, G, visited):
    """深さ優先探索を行う関数
    posは現在位置、visited[x]は頂点xが青色かどうかを表す真偽値
    """
    # print(pos)
    ans.append(pos)
    visited[pos] = True
    if pos == Y:
        print(*ans)
        exit()
    for i in G[pos]:
        if visited[i] == False:
            dfs(i, G, visited)
            # print(pos)
    # ans.remove(pos)
    # removeでも良いが計算量がO(N)かかる
    # stack的に考えられるのでpopでOK
    ans.pop()


# print(AB)
# print(G)
visited = [False] * (N + 1)
ans = deque()
dfs(X, G, visited)

# print(*ans)
