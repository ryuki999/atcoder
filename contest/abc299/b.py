from collections import defaultdict

N, T = map(int, input().split())
C = list(map(int, input().split()))
R = list(map(int, input().split()))

d = defaultdict(int)
if T in C:
    for i in range(N):
        if C[i] == T:
            d[i] = R[i]
    maxv = 0
    maxidx = -1
    for i, v in d.items():
        if maxv < v:
            maxv = v
            maxidx = i
    print(maxidx + 1)
else:
    for i in range(N):
        if C[i] == C[0]:
            d[i] = R[i]
    maxv = 0
    maxidx = -1
    for i, v in d.items():
        if maxv < v:
            maxv = v
            maxidx = i
    print(maxidx + 1)
