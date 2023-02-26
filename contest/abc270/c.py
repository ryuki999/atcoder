from sys import setrecursionlimit
setrecursionlimit(10 ** 6)

N, X, Y = map(int, input().split())
UV = [list(map(int, input().split())) for i in range(N-1)]
# S = input()
# A = list(map(int, input().split()))

def dfs(k, to, q):
    global stop
    if not stop:
        q.append(k)
    if k == to:
        stop = True
    flag[k] = True
    
    sz = len(e[k])
    
    for i in range(sz):
        if not flag[e[k][i]]:
            dfs(e[k][i], to, q)

    if not stop:
        q.pop(-1)
    return q

e = [[] for _ in range(N+1)]
for i in range(N-1):
    e[UV[i][0]].append(UV[i][1])
    e[UV[i][1]].append(UV[i][0])

flag = [False for i in range(N+1)]

stop = False
q = []

dfs(X, Y, q)

print(*q)