import copy

N = int(input())
A = list(map(int, input().split()))

A_copy = copy.copy(A)

A_copy = sorted(A_copy, reverse=True)

for i in range(N):
    if A[i] == A_copy[1]:
        print(i + 1)
        exit()
