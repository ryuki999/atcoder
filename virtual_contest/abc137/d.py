N, M = map(int, input().split())
AB = [list(map(int, input().split())) for _ in range(N)]

d = [0] * (100)
# d = [0] * 10**5
for i in range(N):
    d[AB[i][0]] += AB[i][1]

print(d)
