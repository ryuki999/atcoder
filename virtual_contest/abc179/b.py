N = int(input())
D = [list(map(int, input().split())) for _ in range(N)]

flag = False
c = 0
for d1, d2 in D:
    if d1 == d2:
        c += 1
    else:
        c = 0
    if c == 3:
        flag = True

if flag:
    print("Yes")
else:
    print("No")
