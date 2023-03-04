N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

P = [0] * (N+2)
P[1] = A[0]

for i in range(2, N):
    P[i] = min(P[i-1]+A[i-1], P[i-2]+B[i-2])

# print(P)

place = N
ans = []
while True:
    ans += [place]
    if place == 1:
        break
    if P[place-2] + A[place-2] == P[place-1]:
        place -= 1
    else:
        place -= 2

ans.sort()
print(len(ans))
print(*ans)
# print(P[N-1])