import copy
import sys

# import numpy as np

K = int(input())

h = 21
m = 0

h += int(K/60)
m = str(m + K % 60)
if len(m) == 1:
    m = "0"+m

print(f"{h}:{m}")
