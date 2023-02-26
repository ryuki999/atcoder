import math
N = int(input())

c = 0
d = 2
while d*d <= N:
    while N % d == 0:
        c += 1
        N //= d
    d += 1

if N > 1:
    c += 1

ans = 0
while c > 1:
    ans += 1
    c = c//2 + c%2
print(ans)