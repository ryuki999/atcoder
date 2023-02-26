import copy
import sys
import numpy as np
from collections import defaultdict

# L1, R1, L2, R2 = map(int, input().split())
N = int(input())
# A = list(map(int, input().split()))
A = [list(i.strip()) for i in sys.stdin.readlines()]


for i in range(N):
    for j in range(N):
        if A[i][j] == "W" and A[j][i] != "L":
            print("incorrect")
            exit()
        if A[i][j] == "L" and A[j][i] != "W":
            print("incorrect")
            exit()
        if A[i][j] == "D" and A[j][i] != "D":
            print("incorrect")
            exit()

print("correct")