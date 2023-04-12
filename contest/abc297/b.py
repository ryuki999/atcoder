import copy
import math
from collections import defaultdict

# S = [list(input()) for i in range(8)]
S = input()

flag = True
b = []
for i in range(len(S)):
    if S[i] == "B":
        b.append(i+1)

if b[0] % 2 == b[1] %2:
    flag = False

# print(b)

r = []
for i in range(len(S)):
    if S[i] == "R":
        r.append(i+1)
    if S[i] == "K":
        k = i+1

# print(k, r)
if k > r[0] and k < r[1]:
    pass
else:
    flag = False

if flag:
    print("Yes")
else:
    print("No")