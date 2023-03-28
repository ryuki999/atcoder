N, M = map(int, input().split())
AB = []
for _ in range(N):
    a, b = input().split()
    AB.append([int(a), b])

# for l in range(L):
ans = 0
for i in range(N):
    if AB[i][1] == "E":
        ans = max(ans, L - AB[i][0])
    if AB[i][1] == "W":
        ans = max(ans, AB[i][0])

print(ans)
