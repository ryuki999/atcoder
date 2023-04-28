import math

N, D = map(int, input().split())
X = [list(map(int, input().split())) for _ in range(N)]

ans = 0
for i in range(N):
    for j in range(i, N):
        num = 0
        for k in range(D):
            num += (X[i][k] - X[j][k]) ** 2
        num = math.sqrt(num)
        # print(num)
        if num.is_integer() and num != 0:
            ans += 1
print(ans)
