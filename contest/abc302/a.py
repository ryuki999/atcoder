A, B = map(int, input().split())
# N = int(input())
# S = input()
# C = list(map(int, input().split()))
# AB = [list(map(int, input().split())) for _ in range(N)]

if A % B == 0:
    print(A // B)
else:
    print(A // B + 1)
