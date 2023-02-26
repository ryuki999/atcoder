import copy
import sys
from collections import defaultdict
import numpy as np

N, X, Y = map(int, input().split())

blue = defaultdict(int)
def red_n(N):
    if N == 1:
        return 1
    blue[N] += X
    return red_n(N-1)

def blue_n(N):
    if N == 1:
        return 1
    red_n(N-1)
    blue[N-1] += Y*blue[N]
    return blue_n(N-1)


print(red_n(N))
print(blue)
for i, v in blue.items():
    for _ in range(v):
        blue_n(i)

print(blue)