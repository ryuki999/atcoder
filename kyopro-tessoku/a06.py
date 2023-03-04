N, Q = map(int, input().split())
A = list(map(int, input().split()))
LR = [list(map(int, input().split())) for _ in range(Q)]

T = [0]
t = 0
for i in range(N):
    t += A[i]
    T.append(t)

# print(T)

for l, r in LR:
    print(T[r] - T[l-1])