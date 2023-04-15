N = int(input())
h = list(map(int, input().split()))

P = [0] * (N+2)
P[1] = abs(h[0]-h[1])

for i in range(2, N):
    P[i] = min(P[i-1]+abs(h[i-1]-h[i]), P[i-2]+abs(h[i-2]-h[i]))

# print(P)

place = N
ans = []
while True:
    ans += [place]
    if place == 1:
        break
    if P[place-2] + abs(h[place-2]-h[place-1]) == P[place-1]:
        place -= 1
    else:
        place -= 2

ans.sort()
print(len(ans))
print(*ans)
# print(P[N-1])
