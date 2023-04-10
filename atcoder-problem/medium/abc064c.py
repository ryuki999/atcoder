from collections import defaultdict


N = int(input())
a = list(map(int, input().split()))

rate_dic = defaultdict(int)
r3200 = 0

for i in range(N):
    if a[i] >= 1 and a[i] <= 399:
        rate_dic["gray"] = 1
    elif a[i] >= 400 and a[i] <= 799:
        rate_dic["brown"] = 1
    elif a[i] >= 800 and a[i] <= 1199:
        rate_dic["green"] = 1
    elif a[i] >= 1200 and a[i] <= 1599:
        rate_dic["aqua"] = 1
    elif a[i] >= 1600 and a[i] <= 1999:
        rate_dic["blue"] = 1
    elif a[i] >= 2000 and a[i] <= 2399:
        rate_dic["yellow"] = 1
    elif a[i] >= 2400 and a[i] <= 2799:
        rate_dic["orange"] = 1
    elif a[i] >= 2800 and a[i] <= 3199:
        rate_dic["red"] = 1
    else:
        r3200 += 1

minr = len(rate_dic.keys())
if minr == 0 and r3200 >= 0:
    minr = 1
    maxr = r3200
else:
    maxr = minr+r3200

print(minr, maxr)
