# X, A = map(int, input().split())
S = input()
# W = list(map(str, input().split()))
# AB = [list(map(int, input().split())) for _ in range(N)]

if S[-1] == "s":
    S += "es"
else:
    S += "s"

print(S)
