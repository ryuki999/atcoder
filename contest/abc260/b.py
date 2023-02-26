import copy
import sys
import numpy as np
from collections import defaultdict

N, X, Y, Z = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

A = np.array(A)
B = np.array(B)
C = np.array(A+B)

c = []
for i in range(X):
    for j in range(N):
        if 