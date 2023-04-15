from copy import copy
N = int(input())
A = list(map(int, input().split()))
D = int(input())
LR = [list(map(int, input().split())) for _ in range(D)]

p = [A[0]]
for i in range(1, N):
    p.append(max(p[i-1], A[i]))

rev_A = copy(A[::-1])
q = [rev_A[0]]
for i in range(1, N):
    q.append(max(q[i-1], rev_A[i]))

rev_q = copy(q[::-1])

for i in range(D):
    print(max(p[LR[i][0]-2], rev_q[LR[i][1]]))
