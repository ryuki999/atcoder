N = int(input())
S = input()

s = S.split("-")

# print(s)

if "-" not in S:
    print(-1)
    exit()

ans = len(max(s))
if ans == 0:
    print(-1)
else:
    print(ans)
