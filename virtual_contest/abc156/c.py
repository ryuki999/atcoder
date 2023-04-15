N = int(input())
X = list(map(int, input().split()))

ans = 10**26
for p in range(101):
    m = 0
    for i in range(N):
        m += (X[i] - p) ** 2
    ans = min(ans, m)
print(ans)
