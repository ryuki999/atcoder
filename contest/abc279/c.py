import copy
from collections import defaultdict

H, W = map(int, input().split())
# S = [list(map(int, input().split())) for _ in range(H)]
S = [list(input()) for _ in range(H)]
T = [list(input()) for _ in range(H)]
# st = [list(map(int, input().split())) for i in range(Q)]

S_list = list(zip(*S))
T_list = list(zip(*T))
# print(S_list)
# print(T_list)

t = []
s = []
# for i, j in zip(S_list, T_list):
#     c = 1
#     for ii, jj in zip(i, j):
#         if ii 
#     s.append(i.count("#"))
#     t.append(j.count("#"))

for i in S_list:
    c = 0
    for pos, ii in enumerate(i):
        if ii == "#":
            c += (pos+1)
    s.append(c)

for i in T_list:
    c = 0
    for pos, ii in enumerate(i):
        if ii == "#":
            c += (pos+1)
    t.append(c)

# print(s)
# print(t)

s.sort()
t.sort()

if s == t:
    print("Yes")
else:
    print("No")
