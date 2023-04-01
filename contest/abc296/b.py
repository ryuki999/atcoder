import copy
import math
from collections import defaultdict

S = [list(input()) for i in range(8)]

# print(B)
alpha = ["a", "b", "c", "d", "e", "f", "g", "h"]

for i in range(8):
    for j in range(8):
        if S[i][j] == "*":
            print(f"{alpha[j]}{8-i}")
            exit()