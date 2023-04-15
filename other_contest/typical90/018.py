# 三角関数
import math

T = int(input())
L, X ,Y = map(int, input().split())
Q = int(input())
E = [int(input()) for i in range(Q)]


for e in E:
    theta = e / T * 360
#     print(0, -L/2*math.sin(math.radians(theta)), L/2 - L/2*math.cos(math.radians(theta)))
    a = 0
    a += (0-X)**2
    a += (-L/2*math.sin(math.radians(theta))-Y)**2
    a = math.sqrt(a)

    b = L/2 - L/2*math.cos(math.radians(theta)) - 0
    ans = math.atan2(b, a)
    ans = math.degrees(math.atan2(b, a))
    print(ans)