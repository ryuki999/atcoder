import copy
from collections import Counter

N = int(input())
A = list(map(int, input().split(" ")))

# for a in range(1,N+1):
#     num = A.count(a)
#     if num < 4:
#         print(a)
#         break
a = Counter(A)
for k, v in a.items():
    if v < 4:
        print(k)
