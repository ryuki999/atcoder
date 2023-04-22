"""
自分で考えたこと
黒く塗る頂点をbit全探索
ある黒塗りパターンの時に、クエリの入力(K=2000回)
1.頂点pから最短の黒点までの距離をBFSで求め、dと比較する
全て一致していたらYesかつそのパターンを返す
"""
from collections import deque

N, M = map(int, input().split())
UV = [list(map(int, input().split())) for _ in range(M)]
K = int(input())
PD = [list(map(int, input().split())) for _ in range(K)]

G = [list() for i in range(N + 1)]

# print(AB)
for u, v in UV:
    G[u].append(v)
    G[v].append(u)

for i in range(2**N):
    bin_i = format(i, "b")
    flag = True
    for j in bin_i:
        for p, d in PD:
            dist = [-1] * (N + 1)

            q = deque()
            q.append(1)
            dist[1] = 0

            # print(G)
            # print(dist)
            while len(q) >= 1:
                pos = q.popleft()
                for to in G[pos]:
                    if dist[to] == -1:
                        dist[to] = dist[pos] + 1
                        q.append(to)

            for i in range(1, N + 1):
                # if
                print(dist[i])
