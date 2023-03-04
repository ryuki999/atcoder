N = int(input())

W = 1500
H = 1500
X = [[0] * (W+1) for _ in range(H+1)]
for _ in range(N):
    x, y = list(map(int, input().split()))
    X[x][y] += 1

# XY = [list(map(int, input().split())) for _ in range(N)]

Q = int(input())
ABCD = [list(map(int, input().split())) for _ in range(Q)]

for i in range(H+1):
    for j in range(1, W+1):
        X[i][j] += X[i][j-1]

for j in range(W+1):
    for i in range(1, H+1):
        X[i][j] += X[i-1][j]

for a, b, c, d in ABCD:
    print(X[c][d] + X[a-1][b-1] - X[a-1][d] - X[c][b-1])

