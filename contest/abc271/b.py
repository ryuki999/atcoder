N, Q = map(int, input().split())
# S = input()
# T = input()
# A = list(map(int, input().split()))
al = [list(map(int, input().split())) for i in range(N)]
st = [list(map(int, input().split())) for i in range(Q)]

for s, t in st:
    print(al[s-1][t])