from math import ceil


def divisor_enumeration(N):
    """約数列挙
    N = int(input())
    print(int(sum(divisor_enumeration(N))) - 2)
    """
    ans = []
    for i in range(1, ceil(N ** (1 / 2)) + 1):
        j = N / i
        if j.is_integer():
            ans.append(i)
            ans.append(j)
    return ans


A, B = map(int, input().split())
divA = divisor_enumeration(A)
divB = divisor_enumeration(B)

A_B = sorted(list(set(divA) & set(divB)))
# print(A_B)

ans = []
for i in range(len(A_B)):
    f = True
    for j in range(1, i):
        if A_B[i] % A_B[j] == 0:
            f = False
    if f:
        ans.append(A_B[i])

print(len(ans))
