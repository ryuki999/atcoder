# 順列全探索
import itertools

N = int(input())
A = [list(map(int, input().split())) for i in range(N)]
M = int(input())
XY = [list(map(int, input().split())) for i in range(M)]

grid = [[True] * N for _ in range(N)]
# 仲の悪い組だけFalseにする
for i in range(M):
    grid[XY[i][0] - 1][XY[i][1] - 1] = False
    grid[XY[i][1] - 1][XY[i][0] - 1] = False


per_list = list(itertools.permutations(range(N)))

ans = 10 ** 18

for i in per_list:
    flag = True
    # 仲悪い組が隣り合ってるパターンにflag=False
    for j in range(N - 1):
        if not grid[i[j]][i[j + 1]]:
            flag = False
            break

    cnt = 0 # リレーが可能な時の合計時間
    if flag:
        for j in range(N):
            cnt += A[i[j]][j]
        ans = min(ans, cnt)


if ans == 10 ** 18:
    print(-1)
else:
    print(ans)