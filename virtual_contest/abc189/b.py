N, X = map(int, input().split())
VP = [list(map(int, input().split())) for _ in range(N)]

t = 0
c = 0
for v, p in VP:
    t += v * p
    c += 1
    if t > X * 100:
        print(c)
        exit()

print(-1)
