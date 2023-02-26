import copy
import sys

import numpy as np

N= int(input())
A = [list(map(int, list(i.strip()))) for i in sys.stdin.readlines()]

A = np.array(A)
max_index = np.unravel_index(np.argmax(A), A.shape)

current_x, current_y = max_index
ans = 0
max_n = 0
for i in range(N):
    for j in range(N):
        for x in range(-1, 2):
            for y in range(-1, 2):
                if (x, y) == (0, 0):
                    continue
                direction_x = x
                direction_y = y

                tot = A[(i, j)]
                for _ in range(N-1):
                    tot *= 10
                    i += direction_x
                    j += direction_y
                    i = i % N
                    j = j % N
                    if i == -1:
                        i = N-1
                    if j == -1:
                        j = N-1

                    tot += A[(i, j)]
                ans = max(ans, tot)
print(ans)