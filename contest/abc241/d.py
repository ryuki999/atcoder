# import copy
# import itertools
# import sys

# import numpy as np

# N = int(input())

# inputs = sys.stdin.readlines()

# A = []
# for i in inputs:
#     A .append(list(map(int, i.split(" "))))
# # print(A)

# S = []
# for query in A:
#     if len(query) == 2:
#         num, x = query
#         flag = False
#         if len(S) > 0:
#             for i, s in enumerate(S):
#                 if s > x:
#                     S.insert(i, x)
#                     flag = True
#                     break
#         if not flag:
#             S.append(x)
#     else:
#         num, x, k = query
#         sorted_s = np.array(S)

#         if num == 2:
#             fil_s = sorted_s[sorted_s <= x]
#             if len(fil_s) < k:
#                 print("-1")
#             else:
#                 print(fil_s[-(len(sorted_s) - k)])
#         elif num == 3:
#             fil_s = sorted_s[sorted_s >= x]
#             if len(fil_s) < k:
#                 print("-1")
#             else:
#                 print(fil_s[k-1])
#     # print(S)

import copy
import itertools
import sys

import numpy as np

N = int(input())

inputs = sys.stdin.readlines()

A = []
for i in inputs:
    A .append(list(map(int, i.split(" "))))
# print(A)

def function_2(s, x, k):
    fil_s = s[s <= x]
    if len(fil_s) < k:
        print("-1")
        return
    else:
        print(fil_s[-(len(s) - k)])
        return

def function_3(s, x, k):
    fil_s = s[s >= x]
    if len(fil_s) < k:
        print("-1")
        return
    else:
        print(fil_s[k-1])
        return



S = []
for query in A:
    if len(query) == 2:
        num, x = query
        S.append(x)
        S = sorted(S)
    else:
        num, x, k = query
        s = np.array(S)
        if num == 2:
            function_2(s, x, k)
        elif num == 3:
            function_3(s, x, k)
    # print(S)
