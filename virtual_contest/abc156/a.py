from collections import defaultdict

N, R = map(int, input().split())
# S = input()
# W = list(map(str, input().split()))
# AB = [list(map(int, input().split())) for _ in range(N)]

if N >= 10:
    print(R)
else:
    print(R + 100 * (10 - N))
