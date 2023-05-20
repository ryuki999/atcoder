from itertools import permutations

N, M = map(int, input().split())
S = [input() for _ in range(N)]

p = permutations(S)
for item in p:
    count = 0
    for j in range(N - 1):
        c = 0
        for k in range(M):
            if item[j][k] != item[j + 1][k]:
                c += 1
        if c == 1:
            count += 1
    if count == N - 1:
        print("Yes")
        exit()
print("No")
