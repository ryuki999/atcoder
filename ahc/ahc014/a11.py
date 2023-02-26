import time
 
stratTime = time.perf_counter()

# 30,412,328
import copy

class AbstractDrawer(object):
    def __init__(self, XY, loop, top_n, q1_threshhold):
        self.XY = copy.copy(XY)
        self.loop = loop
        self.q1_threshhold = q1_threshhold
        self.top_n = top_n
    
    def draw(self, qs):
        qs_tmp = copy.copy(qs)

        cs = {}

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

                x, rec_type = self.return_x(x_iter, start_cor)
                if rec_type is None:
                    continue

                y_iter = -1
                while True:
                    y_iter += 1
                    if y_iter >= len(self.XY):
                        break

                    q = [start_cor]
                    q = [x] + q

                    y = self.return_y(q, y_iter, rec_type, start_cor)
                    if y is None:
                        continue

                    q = q + [y]
                    if self._search_q1_and_append_qs(qs_tmp, q, rec_type):
                        # self.XY.append(q[0])
                        # qs_tmp.append({rec_type: q})
                        cs[score(q)] = {rec_type: q}

                    endTime = time.perf_counter()
                    runTime = endTime - stratTime
                    if runTime > LIMIT:
                        qs_tmp = self._append_qs(qs_tmp, q, cs)
                        return self.XY, qs_tmp 

        qs_tmp = self._append_qs(qs_tmp, q, cs)
        return self.XY, qs_tmp

    def _append_qs(self, qs_tmp, q, cs):
        if cs == {}:
            return qs_tmp
        cs = dict(sorted(cs.items(), key=lambda i: i[0], reverse=True))
        c = 0
        for _, q in cs.items():
            rec_type, q = list(q.keys())[0], list(q.values())[0]
            if c > self.top_n:
                break
            if not self._contain_target_cor(q[0], q[1]):
                continue
            if not self._contain_target_cor(q[1], q[2]):
                continue
            if not self._contain_target_cor(q[2], q[3]):
                continue
            if not self._contain_target_cor(q[3], q[0]):
                continue

            if self._contain_target_cor(q[0], q[1]) and self._contain_target_cor(q[0], q[3]) and q[0] not in self.XY:
                if sum(j == {rec_type: q} for j in qs_tmp) < 1 and self._check_cor_line(qs_tmp, q, rec_type):
                    self.XY.append(q[0])
                    qs_tmp.append({rec_type: q})
                    c += 1
        return qs_tmp

    def _promise_q1(self, qs_tmp, start_cor):
        x_iter = -1
        while True:
            x_iter += 1
            if x_iter >= len(self.XY):
                break

            x, rec_type = self.return_x(x_iter, start_cor)
            if rec_type is None:
                continue

            y_iter = -1
            while True:
                y_iter += 1
                if y_iter >= len(self.XY):
                    break

                q = [start_cor]
                q = [x] + q

                y = self.return_y(q, y_iter, rec_type, start_cor)
                if y is None:
                    continue

                q = q + [y]
                if self._search_q1_and_append_qs(qs_tmp, q, rec_type, is_promise_q1=True):
                    return True
        return False
    
    def return_x(self, x_iter, start_cor):
        # 傾き正方向
        x = self.XY[x_iter]
        if x == start_cor:
            return x, None
        elif not self.tdd_search_cor(start_cor, direction=1, xy=x):
            return x, "tdd"
        elif not self.odd_search_cor(start_cor, direction=1, xy=x):
            return x, "odd"
        else:
            return x, None

    def return_y(self, q, y_iter, rec_type, start_cor):
        # 傾き負方向
        y = self.XY[y_iter]
        if y in q:
            return None
        elif rec_type == "tdd":
            if not self.tdd_search_cor(start_cor, direction=0, xy=y):
                return y
        elif rec_type == "odd":
            if not self.odd_search_cor(start_cor, direction=-1, xy=y):
                return y
        return None

    def _search_q1_and_append_qs(self, qs_tmp, q, rec_type, is_promise_q1=False):
        q1 = (q[1][0] - (q[1][0] - q[0][0]) - (q[1][0] - q[2][0]), q[1][1] - (q[1][1] - q[0][1]) - (q[1][1] - q[2][1]))

        if  q1[0] < 0 or q1[1] < 0 or q1[0] > N-1 or q1[1] > N-1:
            return False

        if len(q) == 3 and self._contain_target_cor(q1, q[0]) and self._contain_target_cor(q1, q[2]) and q1 not in self.XY:
            q.insert(0, q1)
            if sum(j == {rec_type: q} for j in qs_tmp) < 1 and self._check_cor_line(qs_tmp, q, rec_type):
                if not is_promise_q1:
                    if self.loop < self.q1_threshhold and not self._promise_q1(qs_tmp, q[0]):
                        return False                
                return True
        return False

    def _check_cor_line(self, qs, q, rec_type):
        """既存の四角形の辺上の点ではないか判定"""
        for qsi in qs:
            key, qsi = list(qsi.keys())[0], list(qsi.values())[0]
            if key != rec_type:
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

    def _contain_target_cor(self, cor1, cor2, target_cor=None):
        """座標間にある点がないか判定 or 座標間に他の点がないか判定(target_cor=None)"""

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
        if target_cor is not None:
            for _ in range(distance):
                if cor1 != bc and cor2 != bc and bc == target_cor:
                    return True
                bc = (bc[0]+ x_step, bc[1]+y_step)
            return False
        else:
            for _ in range(distance):
                if cor1 != bc and cor2 != bc and bc in self.XY:
                    return False
                bc = (bc[0]+ x_step, bc[1]+y_step)
            return True

    def tdd_search_cor(self, base_xy, direction, xy):
        if base_xy[direction] == xy[direction] and self._contain_target_cor(base_xy, xy):
            return False
        return True

    def odd_search_cor(self, base_xy, direction, xy):
        if (xy[1] - base_xy[1]) == 0 or (xy[0] - base_xy[0]) == 0:
            return True
        slope = (xy[1] - base_xy[1]) / (xy[0] - base_xy[0])
        if slope == direction and self._contain_target_cor(base_xy, xy):
            return False
        return True


N, M = map(int, input().split())
XY = [tuple(map(int, input().split())) for _ in range(M)]

# XY = sorted(XY, key=lambda x:(x[0], x[1]))

c = (N-1) / 2
w = [[(x-c)**2 + (x-c)**2 + 1 for x in range(N)] for y in range(N)]
S = sum(map(sum, w))

def score(q):
    total = 0
    for t in q:
        total += round(10**6 * (N**2 / M) * (w[t[0]][t[1]] / S))
    return total

qs = []
qso = []
pre_qs = []
top_n = N**3 // 10000

LIMIT = 4.8
loop = 1
q1_threshhold = 1
while True:
# for _ in range(NUM):
    intervel_time = time.perf_counter()
    ad = AbstractDrawer(XY, loop=loop, top_n=top_n, q1_threshhold=q1_threshhold)
    XY, qso  = ad.draw(qso)
    for q in qso:
        if q not in qs:
            qs += [q]

    loop += 1

    endTime = time.perf_counter()
    runTime = endTime - stratTime
    if runTime > LIMIT:
        break
        
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
