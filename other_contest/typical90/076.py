N = int(input())
A = list(map(int, input().split()))

total = sum(A) // 10

c = []
for i in range(N):
    if c < total:
        c += A[i]
    elif c + A[i]

    c += A[i]
