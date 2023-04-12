N, D = map(int, input().split())
# N = int(input())
# S = input()
T = list(map(int, input().split()))
# AB = [list(map(int, input().split())) for _ in range(N)]

for i in range(N-1):
    # for j in range(N):
    if T[i+1] - T[i] <= D:
        print(T[i+1])
        exit()
print(-1)