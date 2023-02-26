import copy
import sys
from collections import Counter

N = int(input())
S = [i.strip() for i in sys.stdin.readlines()]

print(N)
print(S)

for i in S:
    if "######" in i:
        print("Yes")

for i in range(0, N):
    if "######" in S[i]:
        print("Yes")
        sys.exit()
    else:

        sys.exit()

for j in range(0, N):
    if "######" in S[i, j:j+6]:
        print("Yes")
        
