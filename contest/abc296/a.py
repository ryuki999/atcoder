# N, K = map(int, input().split())
N = int(input())
S = input()
# W = list(map(str, input().split()))
# AB = [list(map(int, input().split())) for _ in range(N)]

if "MF" * (N //2) == S or "FM" * (N //2) == S:
    print("Yes")
    exit()
if N %2 == 1:
    if "MF" * (N //2) + "M" == S or "FM" * (N //2) + "F"==S:
        print("Yes")
        exit()

print("No")