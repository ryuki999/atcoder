import copy
from bisect import bisect, bisect_left, bisect_right
from collections import defaultdict

H, W = map(int, input().split())
S = [list(input()) for _ in range(H)]

ans = 0
for i in range(H):
    for j in range(W-1):
        if S[i][j] == "T" and S[i][j+1]=="T":
            S[i][j] = "P"
            S[i][j+1] = "C"
            ans += 1

# print(ans)
for i in S:
    print("".join(i))