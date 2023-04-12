import sys

H, W = map(int, input().split())
S = [list(i.strip()) for i in sys.stdin.readlines()]

# print(H, W, S)
result = []
for i in range(H):
    for j in range(W):
        num = 0
        if S[i][j] == "#":
            result.append("#")
            continue
        for ii in range(i-1,i+2):
            for jj in range(j-1,j+2):                
                if 0 <= ii < H and 0 <= jj < W and S[ii][jj] == "#":
                    num += 1

        result.append(num)

count = 0
for i in range(H):
    for j in range(W):
        print(result[count], end="")
        count += 1
    print()