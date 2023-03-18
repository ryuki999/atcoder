import math
N = int(input())
XY = [list(map(int, input().split())) for _ in range(N)]

MAX = 10**9
dp = [[MAX] * (N+1) for _ in range(2**N+1)]
dp[0][0] = 0

for i in range(2**N):
    for j in range(N):
        if dp[i][j] >= MAX:
            continue

        for k in range(N):
            if (i // 2**k) % 2 == 1:
                continue
        
            distance = math.sqrt((XY[j][0]-XY[k][0])**2+(XY[j][1]-XY[k][1])**2)
            dp[i+2**k][k] = min(dp[i+2**k][k], dp[i][j]+distance)
            # dp[i+1][v] = min(dp[i+1][v], dp[i][j]+1)

# print(dp)
# for i in dp:
#     print(i)

print(dp[2**N-1][0])