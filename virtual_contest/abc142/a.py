# X, A = map(int, input().split())
N = int(input())
# W = list(map(str, input().split()))
# AB = [list(map(int, input().split())) for _ in range(N)]

if N % 2 == 0:
    print((N // 2) / N)
if N % 2 == 1:
    print((N // 2 + 1) / N)
