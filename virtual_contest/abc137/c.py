from collections import defaultdict

N = int(input())
S = [input() for _ in range(N)]

d = defaultdict(int)

for i in range(N):
    S[i] = "".join(sorted(S[i]))

for s in S:
    d[s] += 1

ans = 0
for v in d.values():
    ans += v * (v - 1) // 2
print(ans)
