# ソートして貪欲法
N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

A.sort()
B.sort()

total = 0
for i in range(N):
    total += abs(A[i]-B[i])

print(total)