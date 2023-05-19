N = int(input())
H = list(map(int, input().split()))

ans = 0
c = 0
for i in range(N - 1):
    if H[i + 1] <= H[i]:
        c += 1
    else:
        c = 0
    ans = max(ans, c)
print(ans)
