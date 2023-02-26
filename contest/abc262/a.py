# L1, R1, L2, R2 = map(int, input().split())
S = int(input())
# A = list(map(int, input().split()))
# A = [list(map(int, input().split())) for i in range(M)]

for i in range(0, 100):
    if (S + i) % 4 == 2:
        print(S+i)
        break