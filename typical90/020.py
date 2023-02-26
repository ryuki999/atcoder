# 対数関数の計算、誤差に注意
import math
a, b ,c = map(int, input().split())

# if math.log2(a) < b*math.log2(c):
if a < c**b:
    print("Yes")
else:
    print("No")