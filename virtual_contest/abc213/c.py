"""座標圧縮(座圧):それぞれの要素が「全体の中で何番目に小さいか」を求める方法
A = (8, 100, 33, 12, 6, 1211) → (1, 4, 3, 2, 0, 5)
B = (6, 9, 9, 2, 100) → (1, 2, 2, 0, 3)
abc213c
"""
H, W, N = map(int, input().split())

A = []
B = []
for _ in range(N):
    a, b = map(int, input().split())
    A.append(a)
    B.append(b)

Adic = {}
Bdic = {}

sortedA = sorted(list(set(A)))
sortedB = sorted(list(set(B)))

for i, x in enumerate(sortedA):
    Adic[x] = i + 1
for i, x in enumerate(sortedB):
    Bdic[x] = i + 1

for i in range(N):
    print(Adic[A[i]], Bdic[B[i]])
