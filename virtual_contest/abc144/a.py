A, B = map(int, input().split())
# S = input()
# W = list(map(str, input().split()))
# AB = [list(map(int, input().split())) for _ in range(N)]

if A >= 1 and A <= 9 and B >= 1 and B <= 9:
    print(A * B)
else:
    print(-1)
