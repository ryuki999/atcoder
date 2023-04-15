N, K = map(int, input().split())

A = list(map(int, input().split()))

def check(x):
    sum = 0
    for i in range(N):
        sum += x // A[i]
        if sum >= K:
            return True
    return False

L = 1
R = 10**9

while L < R:
    M = (L + R) // 2
    ans = check(M)
    if not ans:
        L = M + 1
    if ans:
        R = M

print(L)