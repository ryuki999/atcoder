N = int(input())
A = [list(map(int, input().split())) for _ in range(N)]
Q = int(input())
QUERY = [list(map(int, input().split())) for _ in range(Q)]

d = list(range(1, N + 1))
for i in range(Q):
    q, x, y = QUERY[i]
    if q == 1:
        d[x - 1], d[y - 1] = d[y - 1], d[x - 1]
    if q == 2:
        print(A[d[x - 1] - 1][y - 1])

    # print(d)
    # print(A)
