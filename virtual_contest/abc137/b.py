K, X = map(int, input().split())

ans = []
for i in range(-(10**6), 10**6 + 1):
    if i <= X + (K - 1) and i >= X - (K - 1):
        ans.append(i)
print(*ans)
