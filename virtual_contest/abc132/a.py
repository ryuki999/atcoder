from collections import defaultdict

# N, K = map(int, input().split())
S = input()
# W = list(map(str, input().split()))
# AB = [list(map(int, input().split())) for _ in range(N)]

d = defaultdict(int)
for i in S:
    d[i] += 1

if len(d.keys()) == 2:
    for i in d.keys():
        if d[i] != 2:
            print("No")
            exit()
    print("Yes")
else:
    print("No")
