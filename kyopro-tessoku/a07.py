D = int(input())
N = int(input())
LR = [list(map(int, input().split())) for _ in range(N)]

T = [0 for _ in range(D+2)]
for l, r in LR:
    T[l] += 1
    T[r+1] += -1

# print(T)

t = 0
for i in range(1, D+1):
    t += T[i]
    print(t)