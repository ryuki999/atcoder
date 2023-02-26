import copy
import sys

import numpy as np

A, B, C, D = input().split(" ")

if A > C or ((A == C) and (B > D)):
    print("Aoki")
else:
    print("Takahashi")
