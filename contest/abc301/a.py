# N, A, B = map(int, input().split())
N = int(input())
S = input()
# C = list(map(int, input().split()))
# AB = [list(map(int, input().split())) for _ in range(N)]

A = 0
T = 0
for i in range(N):
    if S[i] == "A":
        A += 1
        if A >= len(S) // 2:
            print("A")
            exit()
    if S[i] == "T":
        T += 1
        if T >= len(S) // 2:
            print("T")
            exit()
