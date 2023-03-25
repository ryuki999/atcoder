from collections import OrderedDict, defaultdict, deque

N, Q = map(int, input().split())

E = [list(map(int, input().split())) for i in range(Q)]

c = 0
member = {}
# member = OrderedDict()
for i in range(Q):
    ev = E[i]
 
    if ev[0] == 1:
        c += 1
        member[c] = c
    elif ev[0] == 2:
        del member[ev[1]]
    else:
        print(next(iter(member)))
    
    # print(member)