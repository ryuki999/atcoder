N, M = map(int, input().split())
X = list(map(int, input().split()))

# 頂点(点)Mと辺(点間の差)M-1とみる
# N点選択すると、未到達の点はM-Nとなる
# M-1辺の中から、M-N辺選べば全ての点に訪れることができる
# そのため、小さい順にソートして、M-N辺を合計すれば良い。
X = sorted(X)
# print(X)

dif = []
for i in range(M - 1):
    dif.append(abs(X[i] - X[i + 1]))
# print(dif)

dif = sorted(dif)

if M - N < 0:
    ans = 0
else:
    ans = sum(dif[: M - N])
print(ans)
