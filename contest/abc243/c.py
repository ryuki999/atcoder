import copy
import sys

import numpy as np

L, R = map(int, input().split(" "))

gcd = []
for x in range(L, R):
    for y in range(x+1, R+1):
        gcd += y-x

print(np.max(gcd))
