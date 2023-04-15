

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
    
N, Q = map(int, input().split())
QUERY = [list(map(int, input().split())) for _ in range(Q)]

UF = UnionFind(N)
for i in range(Q):
    q, u, v = QUERY[i]
    if q == 1:
        UF.unite(u, v)
    if q == 2:
        if UF.same(u, v):
            print("Yes")
        else:
            print("No")