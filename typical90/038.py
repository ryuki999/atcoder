# 最小公倍数
import math

A, B = map(int, input().split())

limit = 10 ** 18
ans = A*B // math.gcd(A, B)
if ans > limit:
    print("Large")
else:
    print(ans)
