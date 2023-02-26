# https://atcoder.jp/contests/abc271/editorial/4937

import itertools

N = int(input())

A = list(map(int, input().split()))

# zyun = list(itertools.permutations(A))
# zyun.sort()

# print(*zyun[zyun.index(A)-1])

pre = 999
for i in range(N-1, -1, -1):
    if pre < A[i]:
        break
    else:
        pre = A[i]

if A[:i] != []:
    print(*A[:i], end=" ")

for j in range(1, N):
    if (A[i] - j) in A[i+1:]:
        cen = A[i] - j
        break

A[A.index(cen)] = A[i]
A[i] = cen

print(A[i], end=" ")

back = A[i+1:]
back.sort(reverse=True)
print(*back)
