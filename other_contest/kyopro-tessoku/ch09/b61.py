from collections import defaultdict
N, M = map(int, input().split())
AB = [list(map(int, input().split())) for _ in range(M)]

d = defaultdict(list)
# d = [[0]*N for _ in range(N)]

# print(AB)
for i in range(M):
    A = AB[i][0]
    B = AB[i][1]
    d[A].append(B)
    d[B].append(A)

# d = sorted(d.items(), key=lambda i: i[0])
# print(d)
ans = 0
ans_max = 0
for i, v in d.items():
    if ans_max < len(v):
        ans = i
        ans_max = len(v)
    # print(f'{i}: {set(v)}')
print(ans)