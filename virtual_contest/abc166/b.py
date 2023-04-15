from collections import defaultdict
N, K = map(int, input().split())
d = []
A = []
for _ in range(K):
    d.append(int(input()))
    A.append(list(map(int, input().split())))

d = defaultdict(list)
for i in range(K):
    for a in A[i]:
        d[a].append(i)

# print(d)
c = 0
for i in range(N):
    if len(d[i+1]) == 0:
        c+=1
print(c)      