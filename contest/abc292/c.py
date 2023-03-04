import copy
from bisect import bisect_left
from collections import defaultdict

N = int(input())
# S = input()

# t = 0
# for i in range(2, N-1):
#     t += (i-1) * (N-i-1)
#     # print(i-1, N-i-1)

# print(t)


tt = {}
for nn in range(1, N):
    t = []
    for i in range(1, int(nn**(1/2))+1):
        if nn % i == 0:
            j = nn // i
            if i * j == nn:
                # print(f"{n} = {i} * {j}")
                t.append((i,j))
                t.append((j,i))
            
    # tt.append(t)
    tt[nn] = list(set(t))

total = 0
for i in range(1, N):
    total += len(tt[i]) * len(tt[N-i])

# print(tt)
print(total)