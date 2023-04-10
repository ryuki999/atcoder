from collections import defaultdict

N = int(input())
D = list(map(int, input().split()))
M = int(input())
T = list(map(int, input().split()))

d = defaultdict(int)
for i in D:
    d[i] += 1
for i in T:
    if d[i] <= 0:
        print("NO")
        exit()
    else:
        d[i] -= 1
print("YES")
