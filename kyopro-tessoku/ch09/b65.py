import sys

# 再帰呼び出しの深さの上限を 120000 に設定
sys.setrecursionlimit(10**6)

def dfs(pos):
    """深さ優先探索を行う関数
    posは現在位置、visited[x]は頂点xが青色かどうかを表す真偽値
    """
    visited[pos] = True
    ans[pos] = 0
    for i in range(len(G[pos])):
        nex = G[pos][i]
        if visited[nex] == False:
            ret = dfs(nex)
            ans[pos] = max(ans[pos], ret+1)
    return ans[pos]

N, T = map(int, input().split())
AB = [list(map(int, input().split())) for _ in range(N-1)]

G = [list() for _ in range(N+1)]
for a, b in AB:
    G[a].append(b)
    G[b].append(a)

# print(G)

visited = [False] * (N+1)
ans = [0] * (N+1)

dfs(T)

print(*ans[1:])