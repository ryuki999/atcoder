N, M, B = map(int, input().split())
A = list(map(int, input().split()))
C = list(map(int, input().split()))

t = 0
for i in range(M):
    t += C[i] * N

for i in range(N):
    t += A[i] * M

t += B * N * M

print(t)
