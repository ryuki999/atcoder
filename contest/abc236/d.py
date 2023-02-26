import copy
import itertools
import sys

N = int(input())

inputs = sys.stdin.readlines()

combinations = list(itertools.combinations(range(2*N), 2))
combinations = list(itertools.combinations(combinations, 2))

A = []
for i in inputs:
    A += list(map(int, i.strip().split(" ")))
# print(A)
print(combinations)

combinations_copy = copy.copy(combinations)
# print([i for i in combinations_copy])

max_list = []
for (x,y),(x1,y1) in combinations:
    if x != x1 and y != y1 and x != y1 and y != x1:
        print(x,y, x1,y1)
        max_list.append(A[x+ y] + A[x1 + y1])

print(max(max_list))

# max_list = []
# for x in range(2*N):
#     for y in range(2*N):
#         if x != (y-2*N-1):
#             # print(x,y, x1,y1)
#             max_list.append(A[x] + A[y])
#         else:
#             break

# print(max(max_list))
