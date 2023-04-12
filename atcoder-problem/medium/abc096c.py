import sys
H, W = map(int, input().split())
S = [list(i.strip()) for i in sys.stdin.readlines()]


for i in range(H):
    for j in range(W):
        flag = False
        if S[i][j] == "#" and j+1<W and S[i][j+1] == "#":
            flag = True
        if S[i][j] == "#" and i+1<H and S[i+1][j] == "#":
            flag = True
        if S[i][j] == "#" and j-1>=0 and S[i][j-1] == "#":
            flag = True
        if S[i][j] == "#" and i-1>=0 and S[i-1][j] == "#":
            flag = True

        if S[i][j] == "#" and not flag:
            print("No")
            exit()

print("Yes")