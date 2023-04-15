H, W, N = map(int, input().split())
ABCD = [list(map(int, input().split())) for _ in range(N)]

ans = [[0] * (W+1) for _ in range(H+1)]

for a, b, c, d in ABCD:
    ans[a-1][b-1] += 1
    ans[c][d] += 1
    ans[c][b-1] -= 1
    ans[a-1][d] -= 1

for i in range(H):
    for j in range(W-1):
        ans[i][j+1] += ans[i][j]
        
for i in range(H-1):
    for j in range(W):
        ans[i+1][j] += ans[i][j]

for i in range(H):
  for j in range(W):
    print(ans[i][j], end=" ")
  print()