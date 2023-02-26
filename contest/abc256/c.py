import copy
import sys

import numpy as np

h1, h2, h3, w1, w2, w3 = map(int, input().split())
lis = [i for i in range(1, 31)]
ans = 0


for a in range(1, 31):
    for b in range(1, 31):
        for d in range(1, 31):
            for e in range(1, 31):
                c = h1 - a - b
                f = h2 - d - e
                g = w1 - a - d
                h = w2 - b - e
                i = w3 - c - f
                if min(c, f, g, h, i) > 0 and g + h + i == h3:
                    ans += 1

print(ans)
