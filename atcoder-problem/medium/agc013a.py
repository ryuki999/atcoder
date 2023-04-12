N = int(input())
A = list(map(int, input().split()))

d = 0
count = 1

for i in range(N-1):
    e = A[i+1] - A[i]
    if  d*e < 0:
        count += 1
        d = 0
    elif d == 0:
        d = e

print(count)