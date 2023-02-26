import copy
from collections import Counter

N, M = map(int, input().split(" "))
A = list(map(int, input().split(" ")))
B = list(map(int, input().split(" ")))

flag = True
for b in B:
    count = A.count(b)
    if count > 0:
        A.pop(A.index(b))
    else:
        flag = False
        break
if flag:
    print("Yes")
else:
    print("No")
