# 14,165,133
import copy
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
       
    for i in range(cor1[0], cor2[0]):
        if (i, cor1[1]) in XY:
            return False
    for i in range(cor1[1], cor2[1]):
        if (cor1[0], i) in XY:
            return False

    return True

def search_cor(base_xy, xory, q):
    if xory == 1:
        not_xory = 0
    else:
        not_xory = 1
    min_dis = 10**9
    min_xy = 0
    flag = False
    for xy in XY:
        dis = abs(base_xy[xory] - xy[xory])
        if base_xy[not_xory] == xy[not_xory] and xy not in q and min_dis > dis:
            min_dis = min(dis, min_dis)
            min_xy = copy.copy(xy)
            flag = True
    if flag and check_line(base_xy, min_xy):
        return min_xy
    else:
        return None

# sorted_xy = sorted(xy, key=lambda x:(x[0], x[1]))

qs = []
i = -1
while True:
    i += 1
    if i == M:
        break
    start_cor = XY[i]
    q = [start_cor]

    # x方向
    xy = search_cor(start_cor, xory=0, q=q)
    if xy is not None:
        q.insert(0, xy)
    else:
        continue

    # y方向
    xy = search_cor(start_cor, xory=1, q=q)
    if xy is not None:
        q.insert(2, xy)
    else:
        continue

    q1 = (q[0][0], q[2][1])
    if len(q) == 3 and check_line(q1, q[0]) and check_line(q1, q[2]) and q1 not in XY:
        q.insert(0, q1)
        qs.append(q)
        break

print(len(qs))
if len(qs) > 0:
    total = 0
    for q in qs:
        total += score(q)
        for t in q:
            print(*t, end=" ")
    print()
    # print(total)
