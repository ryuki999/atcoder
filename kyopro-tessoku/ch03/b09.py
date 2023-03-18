"""
この問題の解答あってるのか？
二枚目の紙が点になっている気がするが...
"""
import math
N = int(input())
ABCD = [list(map(int, input().split())) for _ in range(N)]

XY = 1500

ans = [[0] * (XY+2) for _ in range(XY+2)]

for a, b, c, d in ABCD:
    ans[a][b] += 1
    ans[c+1][d+1] += 1
    ans[c+1][b] -= 1
    ans[a][d+1] -= 1

for i in range(XY):
    for j in range(XY-1):
        ans[i][j+1] += ans[i][j]
        
for i in range(XY-1):
    for j in range(XY):
        ans[i+1][j] += ans[i][j]

# print(sum(map(sum, ans)))
# for i in range(5):
#   for j in range(5):
#     print(ans[i][j], end=" ")
#   print()

num = 0
for i in range(XY):
  for j in range(XY):
    if ans[i][j] >= 1:
      num += 1
print(num)

# 入力
# N = int(input())
# A = [ None ] * N
# B = [ None ] * N
# C = [ None ] * N
# D = [ None ] * N
# for i in range(N):
# 	A[i], B[i], C[i], D[i] = map(int, input().split())

# # 各紙について +1/-1 を加算
# T = [ [ 0 ] * 1501 for i in range(1501) ]
# for i in range(N):
# 	T[A[i]][B[i]] += 1
# 	T[A[i]][D[i]] -= 1
# 	T[C[i]][B[i]] -= 1
# 	T[C[i]][D[i]] += 1

# # 累積和をとる
# for i in range(0, 1501):
# 	for j in range(1, 1501):
# 		T[i][j] = T[i][j-1] + T[i][j]
# for i in range(1, 1501):
# 	for j in range(0, 1501):
# 		T[i][j] = T[i-1][j] + T[i][j]

# # 面積を数える
# Answer = 0
# for i in range(1501):
#   for j in range(1501):
#     if T[i][j] >= 1:
#       Answer += 1

# for i in range(5):
#   for j in range(5):
#     print(T[i][j], end=" ")
#   print()

# # 出力
# print(Answer)
