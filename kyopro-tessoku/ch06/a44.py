N, Q = map(int, input().split())
QUERY = [list(map(int, input().split())) for _ in range(Q)]

A = list(range(1, N + 1))
# print(QUERY)
# print(A)
reverse = False

for i in range(Q):
    q = QUERY[i][0]
    if q == 1:
        x, y = QUERY[i][1], QUERY[i][2]
        if not reverse:
            A[x - 1] = y
        else:
            A[N - x] = y
    if q == 2:
        # A = A[::-1]
        reverse = not reverse
    if q == 3:
        x = QUERY[i][1]
        if not reverse:
            print(A[x - 1])
        else:
            print(A[N - x])

    # print(A)
