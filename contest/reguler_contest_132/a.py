import sys

n = int(input())
R = list(map(int, input().split(" ")))
C = list(map(int, input().split(" ")))

q = int(input())

inputs = sys.stdin.readlines()

matrix = [["o" for _ in range(n)] for _ in range(n)]
# print(matrix)

rev_num = range(1, n+1)[::-1]


judge = int(n/2) + 1
for count, max_ in enumerate(rev_num):

    max_y_idx = R.index(max_)
    max_x_idx = C.index(max_)
    
    min_y_idx = R.index(count + 1)
    min_x_idx = C.index(count + 1)
    
    for i in range(n):
        if  matrix[max_y_idx][i] != ".":
            matrix[max_y_idx][i] = "#"
        if  matrix[i][max_x_idx] != ".":
            matrix[i][max_x_idx] = "#"

    for i in range(n):
        if  matrix[min_y_idx][i] != "#":
            matrix[min_y_idx][i] = "."
        if  matrix[i][min_x_idx] != "#":
            matrix[i][min_x_idx] = "."

    if judge < count:
        break

for i in inputs:
    idx = list(map(int, i.strip().split(" ")))
    print(matrix[idx[0]-1][idx[1]-1], end="")
print()

# for m in matrix:
#     for ma in m:
#         print(ma, end="")
#     print()
