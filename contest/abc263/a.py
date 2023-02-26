import collections
A = map(int, input().split())
# S = int(input())
# A = list(map(int, input().split()))
# A = [list(map(int, input().split())) for i in range(M)]
c = collections.Counter(A)
for s, i in c.items():
    if i == 3:
        continue
    elif i == 2:
        continue
    else:
        print("No")
        exit()
print("Yes")