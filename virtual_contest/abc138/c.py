# from bisect import bisect_left, bisect_right
from collections import deque

N = int(input())
v = list(map(int, input().split()))

v = sorted(v,reverse=True)
ans = 0
q = deque()
for i in v:
    q.append(i)

while len(q) > 1:
    v1 = q.pop()
    v2 = q.pop()
    q.append((v1+v2)/2)

ans = q.pop()
print(ans)