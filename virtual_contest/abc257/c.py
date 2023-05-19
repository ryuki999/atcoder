N = int(input())
S = input()
W = list(map(int, input().split()))

d = []
for i in range(N):
    d.append([W[i], S[i]])

d = sorted(d, key=lambda x: x[0])
# print(d)

count = S.count("1")
ans = S.count("1")
for i in range(N):
    # print(count)
    if d[i][1] == "0":
        count += 1
    if d[i][1] == "1":
        count -= 1
    # 次のやつと同じ場合はそこで線が引けないから
    if i + 1 >= N:
        ans = max(ans, count)
    if i + 1 < N and d[i][0] != d[i + 1][0]:
        ans = max(ans, count)

print(ans)
