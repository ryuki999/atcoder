import copy
import sys
from collections import defaultdict

L1, R1, L2, R2 = map(int, input().split())
# S = input()
# A = list(map(int, input().split()))
# A = [list(map(int, list(i.strip()))) for i in sys.stdin.readlines()]

a = []
for i in range(L1, R1+1):
    a.append(i)

b = []
for i in range(L2, R2+1):
    b.append(i)

num = len(set(a) & set(b))
if num < 1:
    print(0)
else:
    print(num-1)