import copy
import math
from collections import defaultdict

R, C = map(int, input().split())
B = [list(input()) for i in range(R)]

# print(B)

for i in range(R):
    for j in range(C):
        # print(B[i][j])
        for r in range(R):
            for c in range(C):
                if B[i][j] in ["1", "2", "3", "4", "5", "6", "7", "8", "9"]:
                    if (
                        (i, j) != (r, c)
                        and B[r][c] == "#"
                        and abs(i + 1 - (r + 1)) + abs(j + 1 - (c + 1)) <= int(B[i][j])
                    ):
                        B[r][c] = "."
                    # break
        if B[i][j] in ["1", "2", "3", "4", "5", "6", "7", "8", "9"]:
            B[i][j] = "."

for i in B:
    print("".join(i))
