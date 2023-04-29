"""ABC168C
時計の端点の距離を求める問題
ここで使ってる関数はpypyだとエラーになるので注意
"""
import math

A, B, H, M = map(int, input().split())

# 時針と分針の角度を求める
# 時針は時間+分ごとにも動くことを考慮する
Hrad = math.radians(360 * (H * 60 + M) / (12 * 60))
Mrad = math.radians(360 * M / 60)

# print(360 * H / 12, 360 * M / 60)
# print(Hrad, Mrad)
# x座標はsinθ, y座標はcosθで求められる
short = (A * math.sin(Hrad), A * math.cos(Hrad))
long = (B * math.sin(Mrad), B * math.cos(Mrad))

# print(short, long)
print(math.dist(short, long))
