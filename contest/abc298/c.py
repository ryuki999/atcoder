N = int(input())
Q = int(input())
QUERY = [list(map(int, input().split())) for _ in range(Q)]

M = 2 * 10**5 + 1
hako = [[] for _ in range(M)]
card = [set() for _ in range(M)]

for query in QUERY:
    q = query[0]
    if q == 1:
        i, j = query[1], query[2]
        hako[j].append(i)
        card[i].add(j)
    if q == 2:
        i = query[1]
        # tmp = copy.copy(hako[i])
        # heapq.heapify(hako[i])
        # # print(hako[i])
        # for k in range(len(hako[i])):
        #     print(heapq.heappop(hako[i]), end=" ")
        # print()
        # hako[i] = tmp

        print(" ".join(map(str, sorted(hako[i]))))
    if q == 3:
        i = query[1]
        # tmp = copy.copy(card[i])
        # heapq.heapify(card[i])
        # # print(card[i])
        # card[i] = list(set(card[i]))
        # for k in range(len(card[i])):
        #     print(heapq.heappop(card[i]), end=" ")
        # print()
        # card[i] = tmp

        print(" ".join(map(str, sorted(card[i]))))
