# 工夫してfo文を減らす
from collections import deque

N, Q = map(int, input().split())
A = list(map(int, input().split()))
Txy = [list(map(int, input().split())) for i in range(Q)]

ro_c = 0
for i in range(Q):
    t, x, y = Txy[i]
    if t == 1:
        index_x = (x - 1 - ro_c) % N
        index_y = (y - 1 - ro_c) % N
        A[index_x], A[index_y] = A[index_y], A[index_x]
    elif t == 2:
        ro_c += 1
    elif t == 3:
        print(A[((x - 1 - ro_c) % N) % N])
    
    # print(A)