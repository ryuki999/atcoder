# N, K = map(int, input().split())
N = int(input())
S = input()
# W = list(map(str, input().split()))
# AB = [list(map(int, input().split())) for _ in range(N)]

d = {}
d["*"] = []
d["|"] = []

for i in range(N):
    if S[i] == "*" or S[i] == "|":
        d[S[i]].append(i)

if d["*"][0] < d["|"][1] and d["*"][0] > d["|"][0]:
    print("in")
else:
    print("out")
