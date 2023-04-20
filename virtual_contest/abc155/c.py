from collections import defaultdict

N = int(input())
S = [input() for _ in range(N)]

d = defaultdict(int)
for s in S:
    d[s] += 1

dmax = max(d.values())
d = sorted(d.items(), key=lambda x: x[0])
d = sorted(d, reverse=True, key=lambda x: x[1])

# print(d)
for i, v in d:
    if dmax == v:
        print(i)
