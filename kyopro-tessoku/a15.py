from copy import copy
import bisect

N = int(input())
A = list(map(int, input().split()))

setA = copy(list(set(A)))
setA.sort()

# print(setA)

### index検索版(遅い)
# for i in range(N):
#     print(setA.index(A[i])+1, end=" ")
# print()

### 二分探索版(早い)
for i in range(N):
    pos = bisect.bisect_left(setA, A[i])
    if pos < len(setA) and setA[pos] == A[i]:
        print(pos+1, end=" ")
print()