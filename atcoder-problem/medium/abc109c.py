N, X = map(int, input().split())
x = list(map(int, input().split()))


def GCD(A, B):
    while A >= 1 and B >= 1:
        if A >= B:
            A = A % B
        else:
            B = B % A
    if A != 0:
        return A
    return B


ans = abs(x[0] - X)
for i in range(1, N):
    ans = GCD(ans, abs(x[i] - X))
    # print(GCD(A, B))

print(ans)
