Q = int(input())
QUERY = [input().split() for _ in range(Q)]

mp = {}
for i in range(Q):
    if QUERY[i][0] == "1":
        mp[QUERY[i][1]] = QUERY[i][2]
    elif QUERY[i][0] == "2":
        print(mp[QUERY[i][1]])
