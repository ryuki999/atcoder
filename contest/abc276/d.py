import math

N = int(input())

A = list(map(int, input().split()))

g = 0
for i in range(N):
    g = math.gcd(g, A[i])

ans = 0

for i in range(N):
    A[i] /= g
    while(A[i] % 2 == 0):
        A[i] /= 2
        ans += 1
    while(A[i] % 3 == 0):
        A[i] /= 3
        ans += 1
    if(A[i] != 1):
        print(-1)
        exit()
print(ans)
