import math

W, H, x, y = map(int, input().split())

ans = W * H / 2

# 理論的には面積を二等分する線は必ず存在する
# 対角線上の点の場合は答が二つ存在する。
e = 10 ** (-9)
if math.isclose(((H - 0) / (W - 0)) * x, y, rel_tol=e, abs_tol=e) or math.isclose(
    ((0 - H) / (W - 0)) * x + H, y, rel_tol=e, abs_tol=e
):
    print(ans, 1)
else:
    print(ans, 0)
