N, K = map(int, input().split())
H = list(map(int, input().split()))

H = sorted(H, reverse=True)
for i in range(N):
    if H[i] < K:
        i -= 1
        break
print(i + 1)
