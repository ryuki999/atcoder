from collections import defaultdict

M, H = map(int, input().split())
# S = input()
# W = list(map(str, input().split()))
# AB = [list(map(int, input().split())) for _ in range(N)]

if H % M == 0:
    print('Yes')
else:
    print("No")