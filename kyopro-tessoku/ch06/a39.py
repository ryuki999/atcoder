N = int(input())
LR = [list(map(int, input().split())) for _ in range(N)]

# 優先度の低いキー順にソート
LR = sorted(LR, key=lambda x: x[0])
# print(LR)

LR = sorted(LR, key=lambda x: x[1])
# print(LR)

ct = 0
ans = 0
for l, r in LR:
    if ct <= l:
        ct = r
        ans += 1

print(ans)
