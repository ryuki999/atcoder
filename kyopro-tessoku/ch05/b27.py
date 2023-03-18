A, B = map(int, input().split())

def GCD(A, B):
    while A >= 1 and B >= 1:
        if A >= B:
            A = A % B
        else:
            B = B % A
    if A != 0:
        return A
    return B


print(A * B // GCD(A,B))