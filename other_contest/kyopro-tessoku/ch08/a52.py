from collections import deque

Q = int(input())
QUERY = [input().split() for _ in range(Q)]

queue = deque()
for i in range(Q):
    q = QUERY[i][0]
    if q == "1":
        x = QUERY[i][1]
        queue.append(x)
    if q == "2":
        print(queue[0])
    if q == "3":
        ans = queue.popleft()
    # print(queue)
