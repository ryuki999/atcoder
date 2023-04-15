from collections import deque

N, M = map(int, input().split())
ABC = [list(map(int, input().split())) for _ in range(M)]

G = [ list() for i in range(N + 1) ]
for a, b, c in ABC:
	G[a].append((b, c))
	G[b].append((a, c))

MAX = 10**26
cur = [MAX] * (N+1)
kakutei = [False] * (N+1)
cur[1] = 0

while True:
    pos = -1
    min_dist = MAX
    for i in range(1, N+1):
        if kakutei[i] or min_dist <= cur[i]:
            continue
        pos = i
        min_dist = cur[i]
    if pos == -1:
        break
    
    kakutei[pos] = True
    for i in range(len(G[pos])):
        nex = G[pos][i][0]
        cost = G[pos][i][1]
        cur[nex] = min(cur[nex], cur[pos]+cost)

# print(G)
# print(cur)

for i in range(1, N+1):
    if cur[i] == MAX:
        print(-1)
    else:
        print(cur[i])