from collections import deque


Q = int(input())
QUERY = [input().split() for _ in range(Q)]

stack = deque()
for i in range(Q):
    q = QUERY[i][0]
    if q == "1":
        x = QUERY[i][1]
        stack.append(x)
    if q == "2":
        print(stack[-1])
    if q == "3":
        ans = stack.pop()

    # print(stack)
