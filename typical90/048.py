# 上界と下界を見積もる
# 考えられるパターンを網羅して、上から順に足す
N, K = map(int, input().split())
AB = [list(map(int, input().split())) for i in range(N)]

acc = []
for i in range(N):
    acc.append(AB[i][1])
    acc.append(AB[i][0] - AB[i][1])

acc.sort()
# print(acc)
print(sum(acc[::-1][:K]))