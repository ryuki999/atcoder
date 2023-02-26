# 25,579,147
import copy
from collections import defaultdict

# XY = sorted(XY, key=lambda x:(x[0], x[1]))

# c = (N-1) / 2
# w = [[(x-c)**2 + (x-c)**2 + 1 for x in range(N)] for y in range(N)]
# S = sum(map(sum, w))

# def score(q):
#     total = 0
#     for t in q:
#         total += round(10**6 * (N**2 / M) * (w[t[0]][t[1]] / S))
    # return total


class TransverseDirectionDrawer(object):
    def __init__(self, XY):
        self.XY = copy.copy(XY)
    
    def draw(self, qs):
        qs_tmp = copy.copy(qs)
        i = -1
        while True:
            i += 1
            if i >= len(self.XY):
                break
            start_cor = self.XY[i]
            
            x_iter = -1
            while True:
                x_iter += 1
                if x_iter >= len(self.XY):
                    break
                
                # x方向
                x_xy = self.search_cor(start_cor, xory=0, xy=self.XY[x_iter])
                if self.XY[x_iter] == start_cor or x_xy is None:
                    continue

                y_iter = -1
                while True:
                    y_iter += 1
                    if y_iter >= len(self.XY):
                        break

                    q = [start_cor]
                    q = [x_xy] + q


                    # y方向
                    y_xy = self.search_cor(start_cor, xory=1, xy=self.XY[y_iter])
                    if self.XY[y_iter] in q or y_xy is None:
                        continue
                    q = q + [y_xy]

                    q1 = (q[0][0], q[2][1])
                    if len(q) == 3 and self.check_line(q1, q[0]) and self.check_line(q1, q[2]) and q1 not in self.XY:
                        q.insert(0, q1)
                        if sum(j == q for j in qs_tmp) < 1 and self.check_cor_line(qs_tmp, q):
                            self.XY.append(q1)
                            qs_tmp.append(q)
        return self.XY, qs_tmp 

    def check_line(self, cor1, cor2):
        """垂直・水平方向の座標間に他の点がないか判定"""
        step = 1
        if cor1[0] > cor2[0]:
            step = -1

        for i in range(cor1[0], cor2[0], step):
            if cor1 != (i, cor1[1]) and cor2 != (i, cor1[1]) and (i, cor1[1]) in self.XY:
                return False
        step = 1
        if cor1[1] > cor2[1]:
            step = -1

        for i in range(cor1[1], cor2[1], step):
            if cor1 != (cor1[0], i) and cor2 != (cor1[0], i) and (cor1[0], i) in self.XY:
                return False

        return True

    def contain_target_cor(self, cor1, cor2, target_cor):
        """垂直・水平方向の座標間にある点がないか判定"""
        step = 1
        if cor1[0] > cor2[0]:
            step = -1

        for i in range(cor1[0] + step, cor2[0], step):
            # if (i, cor1[1]) == target_cor:
            if cor1 != (i, cor1[1]) and cor2 != (i, cor1[1]) and (i, cor1[1]) == target_cor:
                return True

        step = 1
        if cor1[1] > cor2[1]:
            step = -1

        for i in range(cor1[1] + step, cor2[1], step):
            # if (cor1[0], i) == target_cor:
            if cor1 != (cor1[0], i) and cor2 != (cor1[0], i) and (cor1[0], i) == target_cor:
                return True

        return False

    def check_cor_line(self, qs, q):
        """既存の四角形の辺上の点ではないか判定"""
        cs = defaultdict(int)
        for qi in q:
            for qsi in qs:
                if self.contain_target_cor(qsi[0], qsi[1], qi):
                    return False
                if self.contain_target_cor(qsi[1], qsi[2], qi):
                    return False
                if self.contain_target_cor(qsi[2], qsi[3], qi):
                    return False
                if self.contain_target_cor(qsi[3], qsi[0], qi):
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

    def search_cor(self, base_xy, xory, xy):
        if xory == 1:
            not_xory = 0
        else:
            not_xory = 1
        if base_xy[not_xory] == xy[not_xory] and self.check_line(base_xy, xy):
            return xy
        return None


class ObliqueDirectionDrawer(object):
    def __init__(self, XY):
        self.XY = copy.copy(XY)

    def draw(self, qs):
        qs_tmp = copy.copy(qs)

        i = -1
        while True:
            i += 1
            if i >= len(self.XY):
                break
            start_cor = self.XY[i]
            
            x_iter = -1
            while True:
                x_iter += 1
                if x_iter >= len(self.XY):
                    break
                
                # 傾き正方向
                x_xy = self.search_cor(start_cor, xory=-1, xy=self.XY[x_iter])
                if self.XY[x_iter] == start_cor or x_xy is None:
                    continue

                y_iter = -1
                while True:
                    y_iter += 1
                    if y_iter >= len(self.XY):
                        break

                    q = [start_cor]
                    q = [x_xy] + q

                    # 傾き負方向
                    y_xy = self.search_cor(start_cor, xory=1, xy=self.XY[y_iter])
                    if self.XY[y_iter] in q or y_xy is None:
                        continue
                    q = q + [y_xy]

                    # q1 = (q[0][0]), q[1][1] + (q[0][1] - q[2][1]))
                    q1 = (q[1][0] - (q[1][0] - q[0][0]) - (q[1][0] - q[2][0]), q[1][1] - (q[1][1] - q[0][1]) - (q[1][1] - q[2][1]))
                    if len(q) == 3 and self.check_line(q1, q[0]) and self.check_line(q1, q[2]) and q1 not in self.XY:
                        q.insert(0, q1)
                        if sum(j == q for j in qs_tmp) < 1 and self.check_cor_line(qs_tmp, q):
                            self.XY.append(q1)
                            qs_tmp.append(q)
        return self.XY, qs_tmp 

    def check_line(self, cor1, cor2):
        """斜め方向の座標間に他の点がないか判定"""
        x_step = 1
        if cor1[0] > cor2[0]:
            x_step = -1

        y_step = 1
        if cor1[1] > cor2[1]:
            y_step = -1

        bc = (cor1[0], cor1[1])
        for _ in range(abs(cor1[1] - cor2[1])):
            if cor1 != bc and cor2 != bc and bc in self.XY:
                return False
            bc = (bc[0]+ x_step, bc[1]+y_step)
        return True


    def contain_target_cor(self, cor1, cor2, target_cor):
        """斜め方向の座標間にある点がないか判定"""
        x_step = 1
        if cor1[0] > cor2[0]:
            x_step = -1

        y_step = 1
        if cor1[1] > cor2[1]:
            y_step = -1

        bc = (cor1[0], cor1[1])
        for _ in range(abs(cor1[1] - cor2[1])):
            if cor1 != bc and cor2 != bc and bc == target_cor:
                return True
            bc = (bc[0]+ x_step, bc[1]+y_step)
        return False

    def check_cor_line(self, qs, q):
        """既存の四角形の辺上の点ではないか判定"""
        cs = defaultdict(int)
        for qi in q:
            for qsi in qs:
                if self.contain_target_cor(qsi[0], qsi[1], qi):
                    return False
                if self.contain_target_cor(qsi[1], qsi[2], qi):
                    return False
                if self.contain_target_cor(qsi[2], qsi[3], qi):
                    return False
                if self.contain_target_cor(qsi[3], qsi[0], qi):
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

    def search_cor(self, base_xy, xory, xy):
        if (xy[1] - base_xy[1]) == 0 or (xy[0] - base_xy[0]) == 0:
            return None
        slope = (xy[1] - base_xy[1]) / (xy[0] - base_xy[0])
        if slope == xory and self.check_line(base_xy, xy):
            return xy
        return None


N, M = map(int, input().split())
XY = [tuple(map(int, input().split())) for _ in range(M)]

qs = []
qst = []
qso = []
NUM = 3

for _ in range(NUM):
    tdd = TransverseDirectionDrawer(XY)
    XY, qst  = tdd.draw(qst)
    for q in qst:
        if q not in qs:
            qs += [q]

    odd = ObliqueDirectionDrawer(XY)
    XY, qso  = odd.draw(qso)
    for q in qso:
        if q not in qs:
            qs += [q]


print(len(qs))
# total = 0
for q in qs:
    # total += score(q)
    for t in q:
        print(*t, end=" ")
    print()
# print(total)
