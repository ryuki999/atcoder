from collections import defaultdict

A, B = map(int, input().split())

d = defaultdict(int)
if A - 4 >= 0:
    A -= 4
    d[4] += 1
if A - 2 >= 0:
    A -= 2
    d[2] += 1
if A - 1 >= 0:
    A -= 1
    d[1] += 1


if B - 4 >= 0:
    B -= 4
    d[4] += 1
if B - 2 >= 0:
    B -= 2
    d[2] += 1
if B - 1 >= 0:
    B -= 1
    d[1] += 1

ans = 0
for i, v in d.items():
    if v > 0:
        ans += i
print(ans)
