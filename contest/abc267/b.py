import numpy as np
# N, M = map(int, input().split())
S = input()
# A = list(map(int, input().split()))
# A = [i.strip() for i in sys.stdin.readlines()]

m = [[0 for _ in range(7)] for _ in range(4)]

if S[0] == "1":
    print("No")
    exit()

for i in range(4):
    if i == 0:
        m[i][0] = int(S[6])
        m[i][2] = int(S[7])
        m[i][4] = int(S[8])
        m[i][6] = int(S[9])
    if i == 1:
        m[i][1] = int(S[3])
        m[i][3] = int(S[4])
        m[i][5] = int(S[5])
    if i == 2:
        m[i][2] = int(S[1])
        m[i][4] = int(S[2])
    if i == 3:
        m[i][3] = int(S[0])

m = np.array(m)
# print(m)
for i in range(4):
    for j in range(7):
        if m[i][j] == 1 and j + 1 < 7 and 1 not in m[:,j+1]:
            c = 0
            for k in range(j+1, 7):
                if 1 in m[:,k]:
                    c += 1
                    break
            if c == 1:
                # print(m[:,k])
                print("Yes")
                exit()
print("No")
