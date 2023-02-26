import copy
import sys

import numpy as np

N, K = map(int, input().split())
A = list(map(int, input().split()))
X = [np.array(list(map(int, i.strip().split(" ")))) for i in sys.stdin.readlines()]

distance = []
for i in range(0,N):
    d = []
    if (i+1) not in A:
        for a in range(0,K):
            d.append(np.linalg.norm(X[i]-X[A[a]-1]))
        distance.append(d)

# print(distance)
# print(np.array(distance))
# print(np.max(distance, axis=1))
print(np.max(np.min(distance, axis=1)))
