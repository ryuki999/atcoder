# N, M = map(int, input().split())
N = int(input())
P = list(map(int, input().split()))
# UV = [list(map(int, input().split())) for i in range(M)]

i = N
c = 0
while True:
    if i != 1:
        i = P[i-2]
        c += 1
    else:
        break
print(c)