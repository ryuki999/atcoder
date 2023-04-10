import sys

N = int(input())
TXY = [list(map(int, i.strip().split())) for i in sys.stdin.readlines()]

pre_x = 0
pre_y = 0
pre_t = 0
flag = True
for i in range(N):
    t, x, y = TXY[i]
    if (t-pre_t) >= (abs(x-pre_x) + abs(y-pre_y)) and (t-pre_t) % (abs(x-pre_x) + abs(y-pre_y)) == 0:
        pre_x = x
        pre_y = y
        pre_t = t
        continue
    else:
        flag = False
        break
if flag:
    print("Yes")
else:
    print("No")