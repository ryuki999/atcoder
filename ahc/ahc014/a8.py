# 30,211,224
import copy
from collections import defaultdict


# c = (N-1) / 2
# w = [[(x-c)**2 + (x-c)**2 + 1 for x in range(N)] for y in range(N)]
# S = sum(map(sum, w))

# def score(q):
#     total = 0
#     for t in q:
#         total += round(10**6 * (N**2 / M) * (w[t[0]][t[1]] / S))
    # return total

class AbstractDrawer(object):
    def __init__(self, XY, rec_type):
        self.XY = copy.copy(XY)
        self.rec_type = rec_type

    def _check_line(self, cor1, cor2):
        """座標間に他の点がないか判定"""
        if cor1[0] > cor2[0]:
            x_step = -1
        elif cor1[0] == cor2[0]:
            x_step = 0
        else:
            x_step = 1

        if cor1[1] > cor2[1]:
            y_step = -1
        elif cor1[1] == cor2[1]:
            y_step = 0
        else:
            y_step = 1

        if abs(cor1[1] - cor2[1]) > abs(cor1[0] - cor2[0]):
            distance = abs(cor1[1] - cor2[1])
        else:
            distance = abs(cor1[0] - cor2[0])

        bc = (cor1[0], cor1[1])
        for _ in range(distance):
            if cor1 != bc and cor2 != bc and bc in self.XY:
                return False
            bc = (bc[0]+ x_step, bc[1]+y_step)
        return True

    def _check_cor_line(self, qs, q):
        """既存の四角形の辺上の点ではないか判定"""
        cs = defaultdict(int)
        for qsi in qs:
            key, qsi = list(qsi.keys())[0], list(qsi.values())[0]
            if key != self.rec_type:
                continue
            for qi in range(-1, len(q)-1):
                if self._contain_target_cor(qsi[0], qsi[1], q[qi]):
                    return False
                if self._contain_target_cor(qsi[1], qsi[2], q[qi]):
                    return False
                if self._contain_target_cor(qsi[2], qsi[3], q[qi]):
                    return False
                if self._contain_target_cor(qsi[3], qsi[0], q[qi]):
                    return False

                if (qsi[0] == q[qi] and qsi[1] == q[qi+1]) or (qsi[0] == q[qi+1] and qsi[1] == q[qi]):
                    return False
                if (qsi[1] == q[qi] and qsi[2] == q[qi+1]) or (qsi[1] == q[qi+1] and qsi[2] == q[qi]):
                    return False
                if (qsi[2] == q[qi] and qsi[3] == q[qi+1]) or (qsi[2] == q[qi+1] and qsi[3] == q[qi]):
                    return False
                if (qsi[3] == q[qi] and qsi[0] == q[qi+1]) or (qsi[3] == q[qi+1] and qsi[0] == q[qi]):
                    return False

        return True

    def _contain_target_cor(self, cor1, cor2, target_cor):
        """座標間にある点がないか判定"""

        if cor1[0] > cor2[0]:
            x_step = -1
        elif cor1[0] == cor2[0]:
            x_step = 0
        else:
            x_step = 1

        if cor1[1] > cor2[1]:
            y_step = -1
        elif cor1[1] == cor2[1]:
            y_step = 0
        else:
            y_step = 1

        if abs(cor1[1] - cor2[1]) > abs(cor1[0] - cor2[0]):
            distance = abs(cor1[1] - cor2[1])
        else:
            distance = abs(cor1[0] - cor2[0])

        bc = (cor1[0], cor1[1])
        for _ in range(distance):
            if cor1 != bc and cor2 != bc and bc == target_cor:
                return True
            bc = (bc[0]+ x_step, bc[1]+y_step)
        return False

    def _search_q1_and_append_qs(self, qs_tmp, q):
        q1 = (q[1][0] - (q[1][0] - q[0][0]) - (q[1][0] - q[2][0]), q[1][1] - (q[1][1] - q[0][1]) - (q[1][1] - q[2][1]))

        if  q1[0] < 0 or q1[1] < 0 or q1[0] > N-1 or q1[1] > N-1:
            return qs_tmp

        if len(q) == 3 and self._check_line(q1, q[0]) and self._check_line(q1, q[2]) and q1 not in self.XY:
            q.insert(0, q1)
            if sum(j == {self.rec_type: q} for j in qs_tmp) < 1 and self._check_cor_line(qs_tmp, q):
                self.XY.append(q1)
                qs_tmp.append({self.rec_type: q})
        return qs_tmp
        
class TransverseDirectionDrawer(AbstractDrawer):
    def __init__(self, XY):
        super().__init__(XY=XY, rec_type="tdd")
    
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
                x_xy = self.search_cor(start_cor, direction=1, xy=self.XY[x_iter])
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
                    y_xy = self.search_cor(start_cor, direction=0, xy=self.XY[y_iter])
                    if self.XY[y_iter] in q or y_xy is None:
                        continue
                    q = q + [y_xy]

                    qs_tmp = self._search_q1_and_append_qs(qs_tmp, q)
        return self.XY, qs_tmp 
                
    def search_cor(self, base_xy, direction, xy):
        if base_xy[direction] == xy[direction] and self._check_line(base_xy, xy):
            return xy
        return None


class ObliqueDirectionDrawer(AbstractDrawer):
    def __init__(self, XY):
        super().__init__(XY=XY, rec_type="odd")

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
                x_xy = self.search_cor(start_cor, direction=1, xy=self.XY[x_iter])
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
                    y_xy = self.search_cor(start_cor, direction=-1, xy=self.XY[y_iter])
                    if self.XY[y_iter] in q or y_xy is None:
                        continue
                    q = q + [y_xy]

                    qs_tmp = self._search_q1_and_append_qs(qs_tmp, q)
        return self.XY, qs_tmp 

    def search_cor(self, base_xy, direction, xy):
        if (xy[1] - base_xy[1]) == 0 or (xy[0] - base_xy[0]) == 0:
            return None
        slope = (xy[1] - base_xy[1]) / (xy[0] - base_xy[0])
        if slope == direction and self._check_line(base_xy, xy):
            return xy
        return None


N, M = map(int, input().split())
XY = [tuple(map(int, input().split())) for _ in range(M)]

XY = sorted(XY, key=lambda x:(x[0], x[1]))

qs = []
qst = []
qso = []
NUM = 3

for _ in range(NUM):
    odd = ObliqueDirectionDrawer(XY)
    XY, qso  = odd.draw(qso)
    for q in qso:
        if q not in qs:
            qs += [q]

    tdd = TransverseDirectionDrawer(XY)
    XY, qst  = tdd.draw(qst)
    for q in qst:
        if q not in qs:
            qs += [q]

# print(qs)
print(len(qs))
# total = 0
for q in qs:
    # total += score(q)
    for t in q.values():
        for ti in t:
            print(*ti, end=" ")
    print()
# print(total)
