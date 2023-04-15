import heapq
N, M = map(int, input().split())
ABC = [list(map(int, input().split())) for _ in range(M)]

G = [ list() for i in range(N + 1) ]
for a, b, c in ABC:
	G[a].append((b, c))
	G[b].append((a, c))

INF = 10**26
cur = [INF] * (N+1)
kakutei = [False] * (N+1)
cur[1] = 0
Q = []
heapq.heappush(Q, (cur[1], 1))

while len(Q) >= 1:
    # 次に確定させるべき頂点を求める
    # （ここでは、優先度付きキュー Q の最小要素を取り除き、その要素の 2 番目の値（頂点番号）を pos に代入する）
    pos = heapq.heappop(Q)[1]
    if kakutei[pos]:
        continue
    
    kakutei[pos] = True
    for e in G[pos]:
        if cur[e[0]] > cur[pos] + e[1]:
            cur[e[0]] = cur[pos] + e[1]
            heapq.heappush(Q, (cur[e[0]], e[0]))

# print(G)
# print(cur)

for i in range(1, N+1):
    if cur[i] == INF:
        print(-1)
    else:
        print(cur[i])