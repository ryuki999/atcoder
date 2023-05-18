# X, A = map(int, input().split())
S = input()
T = input()
# W = list(map(str, input().split()))
# AB = [list(map(int, input().split())) for _ in range(N)]

ans = 0
for s, t in zip(S, T):
    if s == t:
        ans += 1
print(ans)
