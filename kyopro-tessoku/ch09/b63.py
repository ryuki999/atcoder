from collections import deque

R, C = map(int, input().split())
sy, sx = map(int, input().split())
gy, gx = map(int, input().split())
c = [list(input()) for _ in range(R)]

MAX = 10**29
dp = [MAX] * (R*C)

q = deque()
q.append((sx-1, sy-1))
dp[(sx-1) * C + sy-1] = 0

while len(q) >= 1:
    pos = q.popleft()
    pos_i = (pos[0]) * C + pos[1]

    poses = [
        (pos[0]+1, pos[1]),
        (pos[0], pos[1]+1),
        (pos[0]-1, pos[1]),
        (pos[0], pos[1]-1)
    ]

    for to in poses:
        to_i = to[0] * C + to[1]

        if dp[to_i] == MAX and c[to[0]][to[1]] != "#":
            dp[to_i] = min(dp[pos_i] + 1, dp[to_i])
            q.append(to)

    # print(len(q))
# print(dp)
# for i in range(0, R*C, C):
#     print(dp[i:i+C])
print(dp[(gy-1) * C + gx-1])

