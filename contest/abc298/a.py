# N, K = map(int, input().split())
N = int(input())
S = input()
# W = list(map(str, input().split()))
# AB = [list(map(int, input().split())) for _ in range(N)]

if S.count("o") >= 1 and S.count("x") == 0:
    print("Yes")
else:
    print('No')