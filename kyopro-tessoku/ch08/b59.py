N = int(input())
A = list(map(int, input().split()))


class SegTree:
    # 要素 dat の初期化を行う（最初は全部ゼロ）
    def __init__(self, n, a):
        self.size = 1
        while self.size < n:
            self.size *= 2
        INF = 10**9
        self.dat = [INF] * (self.size * 2)

    # クエリ1に対する処理
    def update(self, pos, x):
        pos += self.size  # posは0-indexedなので、A[pos]のみに対応するセルの番号はpos + size
        self.dat[pos] = x
        while pos >= 2:
            pos //= 2
            if self.dat[pos * 2] > self.dat[pos * 2 + 1]:
                self.dat[pos] = self.dat[pos * 2] + self.dat[pos * 2 + 1]

    # クエリ2に対する処理
    # uは現在のセル番号、[a,b)はセルに対応する半開区間、[l, r)は求めたい半開区間
    def query(self, l, r, a, b, u):
        if r <= a or b <= l:
            return 0  # 一切含まれない場合
        if l <= a and b <= r:
            return self.dat[u]  # 完全に含まれる場合
        m = (a + b) // 2
        answerl = self.query(l, r, a, m, u * 2)
        answerr = self.query(l, r, m, b, u * 2 + 1)
        return answerl + answerr
