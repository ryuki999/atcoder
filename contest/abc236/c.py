import copy
from collections import Counter

N, M = map(int, input().split(" "))
S = input().split(" ")
T = input().split(" ")

t = 0
for s in range(N):
    if S[s] == T[t]:
        print("Yes")
        t += 1
    else:
        print("No")
