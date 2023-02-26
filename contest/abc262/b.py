import numpy as np

N, M = map(int, input().split())
# N = int(input())
# A = list(map(int, input().split()))
UV = [list(map(int, input().split())) for i in range(M)]

matrix = [[0]*N for i in range(N)]
for u, v in UV:
    matrix[u-1][v-1] = 1
    matrix[v-1][u-1] = 1


# for i in matrix:
#     print(i)
# print(matrix)
print(int(np.sum(np.linalg.matrix_power(matrix, 3).trace()/6)))