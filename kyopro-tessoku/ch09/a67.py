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

N, M = map(int, input().split())
ABC = [list(map(int, input().split())) for _ in range(M)]

sorted_ABC = sorted(ABC, key=lambda x: x[2])

# for i in sorted_ABC:
#     print(i)

UF = UnionFind(N)
cost = 0
for a, b, c in sorted_ABC:
    if not UF.same(a, b):
        UF.unite(a, b)
        cost += c

print(cost)