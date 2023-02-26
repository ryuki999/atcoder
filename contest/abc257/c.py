import copy
import sys

import numpy as np

N = int(input())
# S = int(input())
S = list(map(int, list(input())))
# W = list(map(int, input().split()))
W = list(map(int, input().split()))

S = np.array(S)
W = np.array(W)

arg = np.argsort(W)

arg_s = S[arg]
arg_w = W[arg]

# print(arg_s, arg_w)

m = len(arg_s[arg_s==1])
a = [m]
for i in range(0, N):
    if i != 0 and arg_w[i] != arg_w[i-1]:
        a.append(m)
    if arg_s[i] ==1 :
        m -= 1
    else:
        m +=1

a.append(m)
print(max(a))