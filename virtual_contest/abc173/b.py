from collections import defaultdict

N = int(input())
S = [input() for _ in range(N)]

d = defaultdict(int)
for i in S:
    d[i] += 1

for i in ["AC", "WA", "TLE", "RE"]:
    print(f"{i} x {d[i]}")
