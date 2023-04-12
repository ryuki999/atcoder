K, A, B = map(int, input().split())

ans = 1
if B - A <= 1:
    ans += K
    print(ans)
    exit()

K = K - (A - ans)
ans = A

# print(ans, K)
if K % 2 == 1:
    ans += (B - A) * (K // 2) + 1
if K % 2 == 0:
    ans += (B - A) * (K // 2)

print(ans)
