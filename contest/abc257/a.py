import copy
import sys

import numpy as np

N, X = map(int, input().split())

a = list("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
moji = ""
for i in a:
    moji += i*N

print(moji[X-1])
