N = int(input())
A = [list(map(int, input().split())) for i in range(N)]

total = 1
for i in range(N-1, -1, -1):
    total *= sum(A[i])

print(total % (10**9 + 7))