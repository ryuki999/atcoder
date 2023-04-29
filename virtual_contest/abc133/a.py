N, A, B = map(int, input().split())
# S = input()
# W = list(map(str, input().split()))
# AB = [list(map(int, input().split())) for _ in range(N)]
if B > A * N:
    print(A * N)
else:
    print(B)
