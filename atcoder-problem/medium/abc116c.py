N = int(input())
H = list(map(int, input().split()))

ans = 0
while sum(H) > 0:
    # print(H)
    for l in range(N):
        if H[l] != 0:
            break
    for r in range(l, N + 1):
        if r >= N:
            break
        if H[r] == 0:
            break

    for i in range(l, r):
        H[i] -= 1

    # print(H)
    ans += 1

print(ans)
