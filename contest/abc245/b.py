import copy
import sys

import numpy as np

N = int(input())
A = list(map(int,input().split(" ")))

if max(A) > N:
    a = max(A)
else:
    a = N

for i in range(0, a):
    if i not in A:
        print(i)
        exit()
print(i+1)
