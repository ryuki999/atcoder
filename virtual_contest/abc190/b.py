import math

N, S, D = map(int, input().split())
XY = [list(map(int, input().split())) for _ in range(N)]

ans = 0
for x, y in XY:
    if x < S and y > D:
        ans += y

if ans > 0:
    print("Yes")
else:
    print("No")
# print(ans)
