from collections import defaultdict

N, M = map(int, input().split())
# S = input()
# T = input()
# A = list(map(int, input().split()))
AB = [list(map(int, input().split())) for i in range(M)]
# st = [list(map(int, input().split())) for i in range(Q)]

d = defaultdict(list)

for i, j in AB:
    d[i].append(j)
    d[j].append(i)

# d1 = sorted(d.items(), reverse=True)

for i in range(1, N+1):
    d[i].sort()
    print(len(d[i]), " ".join([str(i) for i in list(d[i])]))
