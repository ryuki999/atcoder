"""
UnionFindでQueryの逆順で解く
最後まで残っている辺は、最初から存在していると同義なので予め追加しないといけない
"""
N, M = map(int, input().split())
AB = [list(map(int, input().split())) for _ in range(M)]

Q = int(input())
QUERY = [list(map(int, input().split())) for _ in range(Q)]

class UnionFind(object):
    def __init__(self, N):
        self.par = [0] * (N+1)
        self.siz = [1] * (N+1)
        for i in range(N+1):
            self.par[i] = -1
            self.siz[i] = 1

    def root(self, x):
        """頂点xの根を返す関数"""
        while True:
            if self.par[x] == -1:
                break
            x = self.par[x]
        return x

    def unite(self, u, v):
        """要素u, vを統合する関数"""
        rootU = self.root(u)
        rootV = self.root(v)
        if rootU == rootV:
            return
        if self.siz[rootU] < self.siz[rootV]:
            self.par[rootU] = rootV
            self.siz[rootV] += self.siz[rootU]
        else:
            self.par[rootV] = rootU
            self.siz[rootU] += self.siz[rootV]
    
    def same(self, u, v):
        """要素uとvが同一のグループかどうかを返す関数"""
        return self.root(u) == self.root(v)

    def different(self, u, v):
        """要素uとvが離れているかどうかを返す関数"""
        return self.root(u) != self.root(v)

UF = UnionFind(N)

ac_v = [True] * (M)
for i in range(Q):
    q = QUERY[i][0]
    if q == 1:
        ac_v[QUERY[i][1]-1] = False

for i in range(M):
    if ac_v[i]:
        UF.unite(AB[i][0], AB[i][1])


ans = []
for i in reversed(range(Q)):
    q = QUERY[i][0]
    if q == 1:
        x = QUERY[i][1] - 1
        UF.unite(AB[x][0], AB[x][1])
    if q == 2:
        u, v = QUERY[i][1], QUERY[i][2]
        if UF.same(u, v):
            # print("Yes")
            ans.append("Yes")
        else:
            # print("No")
            ans.append("No")

for i in ans[::-1]:
    print(i)
