N, K = map(int, input().split())
H = list(map(int, input().split()))

H = sorted(H, reverse=True)

ans = sum(H[K:])
# print(H[K:], H)
print(ans)
