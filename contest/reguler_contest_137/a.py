import copy
import sys
from math import gcd

import numpy as np

# for i in range(1,50):
#     for j in range(i+2, 52):
# # L, R = map(int, input().split(" "))
#         L, R = i, j
#         print(L, R, end="  ")
#         gcd = []
#         for x in range(L, R):
#             for y in range(x+1, R+1):
#                 if np.gcd(x, y) == 1:
#                     gcd += [y-x]
#         ans = np.max(gcd)
#         print(ans, end=" ")

#         flag = False
#         for y in range(R,L, -1):
#             for x in range(L, y):
#                 if np.gcd(x, y) == 1:
#                     print(y-x, end=" ")
#                     ans2 = y-x
#                     # exit()
#                     flag = True
#                     break
#             if flag:
#                 break
#         print(ans==ans2)



"""
横x, 縦y
  3  4  5  6
2 1  △ 3  △
3 x  1  2  △
4 x  x  1  △
5 x  x  x  1
"""
l, r = map(int, input().split())
 
d = r - l # 現時点で想定される最も大きな差
ll = l
while 1:
    # xとd=y-xの最大公約数が1のとき、xとyの最大公約数も1(素数)
    for i in range(l, ll + 1):
        if gcd(i, d) == 1:
            print(d)
            exit()
    # dを1ずつ減らして存在するか確認する
    d -= 1
    ll += 1
