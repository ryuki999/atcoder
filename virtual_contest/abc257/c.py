from bisect import bisect_left, bisect, bisect_right

N = int(input())
S = input()
W = list(map(int, input().split()))

child = []
adult = []
for i in range(N):
    if S[i] == "0":
        child.append(W[i])
    if S[i] == "1":
        adult.append(W[i])

child = sorted(child)
adult = sorted(adult)
print(child, adult)
ans = 0
for i in range(N):
    pos1 = bisect(child, W[i])
    pos2 = bisect_left(adult, W[i])
    print(pos1, pos2)
    # print(pos2 + N - len(adult))
    ans = max(ans, pos2 + N - len(adult))
print(ans)
