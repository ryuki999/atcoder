# https://atcoder.jp/contests/abc271/editorial/4937

N = int(input())
A = set(map(int, input().split()))

l = 0
r = N + 1

while r - l > 1:
    m = (l + r) // 2
    # m巻まで読めるか?
    c = len(set(range(1, m + 1)) & A)
    if c + (N - c) // 2 >= m:
        l = m
    else:
        r = m
print(l)

# N巻まで読める: Nまでの存在する巻+(残りの巻//2)>=N巻
# TLEだから二分探索
# for i in range(1, N+3):
#     c = len(set(range(1, i + 1)) & A)
#     if c + (N-c) // 2 >= i:
#         continue
#     else:
#         break
# print(i-1)
