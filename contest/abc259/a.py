import copy
import sys

N, M, X, T, D = map(int, input().split())

if M >= X:
    print(T)
else:
    a = T - (X-M) *D
    print(a)

# ans = 

# print(f"{h}:{m}")
