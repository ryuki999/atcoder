N, X = map(int, input().split())
A = list(map(int, input().split()))

L = 0
R = len(A)
M = (L + R) // 2

while X != A[M]:
    M = (L + R) // 2
    # print(A[M])
    if X < A[M]:
        R = M - 1
    if X > A[M]:
        L = M + 1

print(M+1)