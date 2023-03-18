from copy import copy

# N, Q = map(int, input().split())
N = int(input())
A = list(map(int, input().split()))
Q = int(input())
LR = [list(map(int, input().split())) for _ in range(Q)]

T = [[0, 0]]
t = [0, 0]
for i in range(N):
    t[A[i]] += 1
    T.append(copy(t))

for l, r in LR:
    w = T[r][1] - T[l-1][1]
    l = T[r][0] - T[l-1][0]
    if w > l:
        print("win")
    elif w == l:
        print("draw")
    else:
        print("lose")

