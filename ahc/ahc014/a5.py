# 17,880,689 
import copy
from collections import defaultdict
N, M = map(int, input().split())
XY = [tuple(map(int, input().split())) for _ in range(M)]

c = (N-1) / 2
w = [[(x-c)**2 + (x-c)**2 + 1 for x in range(N)] for y in range(N)]
S = sum(map(sum, w))

# print(c)
# print(w)
# print(S)

def score(q):
    total = 0
    for t in q:
        total += round(10**6 * (N**2 / M) * (w[t[0]][t[1]] / S))
    return total

def check_line(cor1, cor2):
    """垂直・水平方向の座標間に他の点がないか判定"""
    if cor1[0] > cor2[0]:
        step = -1
    else:
        step = 1
    for i in range(cor1[0], cor2[0], step):
        if cor1 != (i, cor1[1]) and cor2 != (i, cor1[1]) and (i, cor1[1]) in XY:
            # print((i, cor1[1]))
            return False

    if cor1[1] > cor2[1]:
        step = -1
    else:
        step = 1
    for i in range(cor1[1], cor2[1], step):
        if cor1 != (cor1[0], i) and cor2 != (cor1[0], i) and (cor1[0], i) in XY:
            # print((cor1[0], i))
            return False

    return True

def contain_target_cor(cor1, cor2, target_cor):
    """垂直・水平方向の座標間にある点がないか判定"""
    if cor1[0] > cor2[0]:
        step = -1
    else:
        step = 1
    for i in range(cor1[0] + step, cor2[0], step):
        if (i, cor1[1]) == target_cor:
            return True
    if cor1[1] > cor2[1]:
        step = -1
    else:
        step = 1
    for i in range(cor1[1] + step, cor2[1], step):
        if (cor1[0], i) == target_cor:
            return True

    return False


def check_cor_line(qs, q):
    """既存の四角形の辺上の点ではないか判定"""
    cs = defaultdict(int)
    for qi in q:
        for qsi in qs:
            if contain_target_cor(qsi[0], qsi[1], qi):
                return False
            if contain_target_cor(qsi[1], qsi[2], qi):
                return False
            if contain_target_cor(qsi[2], qsi[3], qi):
                return False
            if contain_target_cor(qsi[3], qsi[0], qi):
                return False

            for qsij in qsi:
                if qsij == qi:
                    cs[qi] += 1
    # print(cs)
    if sum(cs.values()) < 2:
        return True
    else:
        return False

    return True

def search_cor(base_xy, xory, q, c_iter):
    if xory == 1:
        not_xory = 0
    else:
        not_xory = 1
    xy = XY[c_iter]
    if base_xy[not_xory] == xy[not_xory] and xy not in q:
        if check_line(base_xy, xy):
            return xy
    return None

# XY = sorted(XY, key=lambda x:(x[0], x[1]))

qs = []

i = -1
while True:
    i += 1
    if i >= len(XY):
        break

    x_iter = -1
    while True:
        x_iter += 1
        if x_iter >= len(XY):
            break
        
        y_iter = -1
        while True:
            y_iter += 1
            if y_iter >= len(XY):
                break

            start_cor = XY[i]
            q = [start_cor]

            # x方向
            xy = search_cor(start_cor, xory=0, q=q, c_iter=x_iter)
            if xy is not None:
                q.insert(0, xy)
            else:
                continue

            # y方向
            xy = search_cor(start_cor, xory=1, q=q, c_iter=y_iter)
            if xy is not None:
                q.insert(2, xy)
            else:
                continue

            q1 = (q[0][0], q[2][1])
            if len(q) == 3 and check_line(q1, q[0]) and check_line(q1, q[2]) and q1 not in XY:
                q.insert(0, q1)
                if sum(j == q for j in qs) < 1 and check_cor_line(qs, q):
                    XY.append(q1)
                    qs.append(q)
                    # break
    
print(len(qs))
if len(qs) > 0:
    total = 0
    for q in qs:
        total += score(q)
        for t in q:
            print(*t, end=" ")
        print()
    # print(total)
