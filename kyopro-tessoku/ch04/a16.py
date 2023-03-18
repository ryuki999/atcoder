N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

P = [0] * (N+2)
P[1] = A[0]
# P[2] = P[1] + A[1]

for i in range(2, N):
    # P[i] = P[i-1] + A[i-1]
    P[i] = min(P[i-1]+A[i-1], P[i-2]+B[i-2])
    # print(P)

print(P[N-1])