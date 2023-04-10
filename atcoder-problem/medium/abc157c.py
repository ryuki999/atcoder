import sys
from collections import defaultdict

N, M  = map(int, input().split())
SC = [list(map(int, i.strip().split())) for i in sys.stdin.readlines()]

for ans in range(0, 1000):
    ans = str(ans)
    if len(ans) != N:
        continue
    
    ok = True
    for i in range(0, M):
        for j in range(0, N):
            if (j == (SC[i][0]-1) and int(ans[j]) != SC[i][1]):
                ok = False
    if ok:
        print(ans)
        exit()

print(-1)