import copy
import sys

import numpy as np

S = np.array(input().split(" "))
T = np.array(input().split(" "))


if sum(S==T) == 0 or sum(S==T) == 3:
    print("Yes")
if sum(S==T) == 1:
    print("No")
