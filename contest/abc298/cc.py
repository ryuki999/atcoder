N = int(input())
Q = int(input())
QUERY = [list(map(int, input().split())) for _ in range(Q)]
M = 2 * 10**5 + 1


box = [[] for _ in range(N + 1)]
card = [set() for _ in range(M)]
for query in QUERY:
    # q = list(map(int, input().split()))
    q = query[0]
    if q == 1:
        i, j = query[1], query[2]
        box[j].append(i)
        card[i].add(j)
    elif q == 2:
        i = query[1]
        print(" ".join(map(str, sorted(box[i]))))
    else:
        i = query[1]
        print(" ".join(map(str, sorted(card[i]))))
