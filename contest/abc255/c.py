import copy
import sys

import numpy as np

# X, A, D, N = map(int, input().split(" "))

# S = [A+D*i- X for i in range(N)]

# print(np.min(np.abs(S)))

X, A, D, N = map(int, input().split())
 
if D == 0:
    ans = abs(X - A)
else:
    if D < 0:
        D = abs(D)
        A = A - D * (N-1)
    # Xが初項A以下の時差分でOK D>0なので増え続けるだけ。X=6, A=12
    if X <= A:
        ans = A - X
    # Xが数列の最大値より大きい時差分でOK これ以上の数はない
    elif X >= A + D * (N-1):
        ans = X - (A + D * (N-1))
    else:
        # print((X-A) % D, D - (X-A) % D)
        ans = min((X-A) % D, D - (X-A) % D)
    # Xが中間の時、
 
print(ans)
