from bisect import bisect_left, bisect_right

N = int(input())
d = list(map(int, input().split()))

d = sorted(d)

K = 10**5 + 1
ans = 0
for i in range(K):
    pos = bisect_right(d, i)
    # print(d, pos, N // 2)

    if pos == N // 2:
        ans += 1

print(ans)
