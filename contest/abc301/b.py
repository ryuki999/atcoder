N = int(input())
A = list(map(int, input().split()))

while True:
    f = True
    for i in range(len(A) - 1):
        if abs(A[i] - A[i + 1]) != 1:
            f = False
            break
    if f:
        break
    # print(i)
    if A[i] < A[i + 1]:
        c = A[i + 1] - A[i]
        for j in range(A[i] + 1, A[i + 1]):
            i += 1
            A.insert(i, j)
    if A[i] > A[i + 1]:
        c = A[i] - A[i + 1]
        for j in range(A[i] - 1, A[i + 1], -1):
            i += 1
            A.insert(i, j)
    # print(*A)
    # break

print(*A)
