import copy
import sys

import numpy as np

a, b, d = map(int, input().split())
theta = d * (np.pi /180) 

ansx = a * np.cos(theta) - b * np.sin(theta)
ansy = a * np.sin(theta) + b * np.cos(theta)


print(ansx, ansy)