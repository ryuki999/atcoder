import heapq

N, D = map(int, input().split())
XY = [list(map(int, input().split())) for _ in range(N)]

# XY = sorted(XY, key=lambda x: x[1], reverse=True)
# XY = sorted(XY, key=lambda x: x[0])
# print(XY)
used = [False] * (N + 1)

ans = 0
for i in range(1, D + 1):
    maxv = 0
    maxidx = 0
    for j in range(N):
        if used[j]:
            continue
        if maxv <= XY[j][1] and i >= XY[j][0]:
            maxv = XY[j][1]
            maxidx = j

    if maxv != 0:
        used[maxidx] = True
        ans += XY[maxidx][1]

print(ans)

# for i in XY:
#     print(i)
