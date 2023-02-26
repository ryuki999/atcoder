import copy
import math
from collections import defaultdict

A, B = map(int, input().split())


def f(i):
    return B * i + A/math.sqrt(i+1)

l = 0
r = A / B

while r - l > 2:
    m1 = (l * 2 + r) // 3
    m2 = (l + r * 2) // 3
    if f(m1) > f(m2):
        l = m1
    else:
        r = m2
ans = A
for i in range(int(l), int(r)):
    ans = min(ans, f(i))

print(ans)
