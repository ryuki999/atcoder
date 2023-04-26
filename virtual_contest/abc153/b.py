H, N = map(int, input().split())
A = list(map(int, input().split()))

A = sorted(A, reverse=True)

sumA = sum(A[:N])
# print(sumA)

if sumA >= H:
    print("Yes")
else:
    print("No")
