import sys

H, W = map(int, input().split())
a = [list(i.strip()) for i in sys.stdin.readlines()]

del_h = []
del_w = []

for i in range(H):
    flags = 0
    for j in range(W):
        if a[i][j] == ".":
            flags += 1
    if flags == W:
        del_h.append(i)

for i in range(W):
    flags = 0
    for j in range(H):
        if a[j][i] == ".":
            flags += 1
    if flags == H:
        del_w.append(i)

for i in range(H):
    if i in del_h:
        continue
    for j in range(W):
        if j in del_w:
            continue
        print(a[i][j], end="")
    print()