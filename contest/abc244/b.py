import copy
import sys

import numpy as np

N = int(input())
T = list(input())
# print(N, T)
cor = [0, 0]
direction = "right"

for i in range(N):
    if T[i] == "S":
        if direction=="right":
            cor[0] += 1
        if direction=="left":
            cor[0] -= 1
        if direction=="top":
            cor[1] += 1
        if direction=="bottom":
            cor[1] -= 1
    elif T[i] == "R":
        if direction=="right":
            direction = "bottom"
        elif direction=="left":
            direction = "top"
        elif direction=="top":
            direction = "right"
        elif direction=="bottom":
            direction = "left"

print(cor[0], cor[1])
