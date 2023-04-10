import numpy as np

N, M = map(int, input().split())

ab = []
for _ in range(N):
    ab.append(list(map(int, input().split())))

cd = []
for _ in range(M):
    cd.append(list(map(int, input().split())))

for a, b in ab:
    min_num = np.inf
    for i, (c, d) in enumerate(cd):
        if min_num > abs(a-c) + abs(b-d):
            min_num = abs(a-c) + abs(b-d)
            min_idx = i+1
    print(min_idx)
