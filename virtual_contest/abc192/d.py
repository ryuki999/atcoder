# from collections import deque
import numpy as np

X = int(input())
M = int(input())

maxA = int(max(list(str(X))))
print(maxA)
ans = 0
for i in (maxA+1,10**5):
    x = 0
    strX = str(X)
    for j in range(len(strX)):
        x += (i**j)*int(strX[len(strX)-j-1])
    # print(np.base_repr(X, base=i))
    print(x)
    if M < x:
        break
    else:
        ans += 1

print(ans)