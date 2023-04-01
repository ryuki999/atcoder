# N, K = map(int, input().split())
N = int(input())
# W = list(map(str, input().split()))
# AB = [list(map(int, input().split())) for _ in range(N)]

if N % 1000 == 0:
    print(0)
else:
    print(1000 - N % 1000)
# if S[2] == S[3] and S[4] == S[5]:
#     print("Yes")
# else:
#     print("No")
