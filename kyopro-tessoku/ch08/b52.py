from collections import deque

N, X = map(int, input().split())
A = list(input())

q = deque()
q.append(X - 1)
A[X - 1] = "@"
# print(q)
while len(q) > 0:
    pos = q.popleft()
    if 0 <= pos - 1 and A[pos - 1] == ".":
        A[pos - 1] = "@"
        q.append(pos - 1)
    if N > pos + 1 and A[pos + 1] == ".":
        A[pos + 1] = "@"
        q.append(pos + 1)

print("".join(A))
