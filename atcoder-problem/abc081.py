from collections import defaultdict

N, K = map(int, input().split())

A = list(map(int, input().split()))

dic = defaultdict(int)

for i in range(N):
    dic[A[i]] += 1

sortdic = sorted(dic.items(), key=lambda x:x[1])

ans = 0
for i in range(len(sortdic)-K):
    ans += sortdic[i][1]

# print(sortdic)
print(ans)