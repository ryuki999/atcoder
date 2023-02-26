import copy
import sys

import numpy as np

N = int(input())
post = [i+1 for i in range(2*N+1)]
# print(post)

while True:
    takahashi = post.pop(0)
    print(takahashi)
    if len(post) < 1:
        print(0)
        exit()
    aoki = int(input())
    # print(aoki)
    post.remove(aoki)
