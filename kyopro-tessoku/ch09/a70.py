from collections import deque

N, M = map(int, input().split())
A = list(map(int, input().split()))
XYZ = [list(map(int, input().split())) for _ in range(M)]

G = [list() for _ in range(2**N)]


for i in range(2**N):
    intA = i
    for j in range(M):
        x = ["0"] * N
        for k in XYZ[j]:
            x[k - 1] = "1"

        intx = int("0b" + "".join(x[::-1]), 2)
        xor_xA = intA ^ intx

        G[intA].append(xor_xA)
        intA = xor_xA
# print(G)

binA = "0b" + "".join(list(map(str, A[::-1])))
intA = int(binA, 2)

q = deque()
q.append(intA)
dist = [-1] * (2**N + 1)
dist[intA] = 0

while len(q) > 0:
    pos = q.popleft()
    for to in G[pos]:
        if dist[to] == -1:
            dist[to] = dist[pos] + 1
            q.append(to)

print(dist[2**N - 1])
