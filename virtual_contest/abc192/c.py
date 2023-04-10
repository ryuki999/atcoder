from bisect import bisect_left, bisect_right

N, K = map(int, input().split())


for i in range(K):
    g1N = sorted(list(str(N)),reverse=True)
    g2N = sorted(list(str(N)),reverse=False)
    N = int("".join(g1N)) - int("".join(g2N))

print(N)