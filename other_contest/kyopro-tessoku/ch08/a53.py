import heapq
Q = int(input())
QUERY = [list(map(int, input().split())) for _ in range(Q)]

T = []
for i in range(Q):
    if QUERY[i][0] == 1:
        heapq.heappush(T, QUERY[i][1])
    elif QUERY[i][0] == 2:
        # ans = heapq.heappop(T)
        # print(ans)
        # heapq.heappush(T, ans)
        print(T[0])
        # T[0]は優先度付きキューの最小要素
        # 例えば小さいほうから2番目の要素がT[1]で取り出せるとは限らないことに注意
    else:
        ans = heapq.heappop(T)

