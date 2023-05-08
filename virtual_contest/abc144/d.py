import math


def find_max_angle(a, b, x):
    # 水筒を傾けずに立てた状態での水の高さを計算
    h = x / (a * a)

    # 水筒を傾けた際の水の体積を計算するための角度θを求める
    if h <= a:
        # 水は底面の一部に触れているだけで、水筒をさらに傾けることができる場合
        l = a
        theta = math.atan(h / l)
    else:
        # 水は底面の対角線上の2つの頂点に触れていて、水筒をさらに傾けると水がこぼれる場合
        h_prime = 2 * x / (a * a)
        l = a / math.sqrt(2)
        theta = math.atan(h_prime / l)

    # 角度θを度数法に変換して答えを求める
    return math.degrees(theta)


# パラメータを入力して、関数を呼び出し、答えを表示する
A, B, X = map(int, input().split())

max_angle = find_max_angle(A, B, X)
print(max_angle)
