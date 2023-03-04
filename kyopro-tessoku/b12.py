N = int(input())

def f(x):
    return x**3 + x


L = 1
R = 100000

while L < R:
    M = (L + R) / 2
    ans = f(M)
    if ans > N:
        R = M
    if ans < N:
        L = M
    if abs(ans - N) <= 0.001:
        break
    # print(L, M, R)

# print(abs(ans - N))
print(M)