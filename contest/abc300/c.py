from collections import defaultdict

H, W = map(int, input().split())
C = [list(input()) for _ in range(H)]

anss = [0] * (min(H, W) + 1)
for a in range(H):
    for b in range(W):
        if C[a][b] != "#":
            continue

        ans = 0
        for n in range(1, min(H, W)):
            if a + n < H and b + n < W and a - n >= 0 and b - n >= 0:
                if (
                    C[a + n][b + n] == "#"
                    and C[a + n][b - n] == "#"
                    and C[a - n][b + n] == "#"
                    and C[a - n][b - n] == "#"
                ):
                    ans += 1
                else:
                    break
        # print(a, b, ans)
        anss[ans] += 1

print(*anss[1:])
