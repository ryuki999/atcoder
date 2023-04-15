import re

Q = int(input())
QUERY = [list(map(int,input().split())) for _ in range(Q)]

MOD = 998244353

s = "1"
for query in QUERY:
    q = query[0]
    if q == 1:
        x = query[1]
        s += str(x)
    if q == 2:
        s = re.sub(r'.', '', s, count = 1)
    if q == 3:
        print(int(s)%MOD)
    # print(s)