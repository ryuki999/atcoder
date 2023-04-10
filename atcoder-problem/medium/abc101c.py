N, K = map(int, input().split())
A = list(map(int, input().split()))

N -= K
ans = 1
while N > 0:
    N -= K - 1
    ans += 1

print(ans)
