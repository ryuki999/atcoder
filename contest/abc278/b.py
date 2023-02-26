import copy
from collections import defaultdict

H, M = map(int, input().split())
# S = input()
# T = input()
# A = list(map(int, input().split()))
# AB = [list(map(int, input().split())) for i in range(M)]
# st = [list(map(int, input().split())) for i in range(Q)]

h_all = [f"{str(i).zfill(2)}" for i in range(0, 24)]
m_all = [f"{str(i).zfill(2)}" for i in range(0, 60)]


if H < 16 and H >= 0:
    print(H, M)
    exit()

if H < 20 and H >= 16:
    print(20, 0)
    exit()

for _ in range(20,24):
    if H > 23:
        H = 0
    for _ in range(0,60):
        if M > 59:
            M = 0
            break
        
        t = f"{str(H).zfill(2)}{str(M).zfill(2)}"
        rt = t[0] + t[2] + t[1] + t[3]
        # print(t, rt)

        if rt[:2] in h_all and rt[2:] in m_all:
            print(H, M)
            # print(f"{str(H).zfill(2)}{str(M).zfill(2)}", " ", rt)
            exit()
        M = M+1
    H = H + 1
