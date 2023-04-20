N, K = map(int, input().split())
A = list(map(int, input().split()))

B = []
for i in range(N):
    for j in range(i + 1, N):
        B.append(A[i] * A[j])

B = sorted(B)
print(B[K - 1])
