A, B, C = map(int, input().split())
# S = input()
# W = list(map(str, input().split()))
# AB = [list(map(int, input().split())) for _ in range(N)]

if C == 0:
    if A > B:
        print("Takahashi")
    else:
        print("Aoki")
else:
    if A < B:
        print("Aoki")
    else:
        print("Takahashi")
