import copy
import sys

import numpy as np

N, K = map(int, input().split(" "))
A = list(map(int,input().split(" ")))
B = list(map(int,input().split(" ")))

pre_items = []
for i in range(0, N-1):
    flag = False
    new_items = []
    if abs(A[i] -A[i+1]) <= K:
        # print(A[i+1])
        new_items.append((A[i], A[i+1]))
        flag = True

    if abs(A[i] -B[i+1]) <= K:
        # print(A[i+1])
        new_items.append((A[i], B[i+1]))
        flag = True

    if abs(B[i] -A[i+1]) <= K:
        # print(B[i+1])
        new_items.append((B[i], A[i+1]))
        flag = True

    if abs(B[i] -B[i+1]) <= K:
        # print(B[i+1])
        new_items.append((B[i], B[i+1]))
        flag = True
    
    if not flag:
        print("No")
        exit()

    # print(pre_items, new_items)
    pre_items_copy = copy.copy(pre_items)
    if i == 0:
        pre_items = copy.copy(new_items)
    else:
        print(np.array(new_items)[:,0])
        print(np.array(pre_items_copy)[:,1])
        pre_items = np.array(new_items)[(np.array(new_items)[:,0] == np.array(pre_items_copy)[:,1]).any()]


if pre_items:
    print("Yes")
else:
    print("No")
