from collections import deque

s = input()
slen = len(s)

q = deque()

for i in s:
    if i == "0" or i == "1":
        q.append(i)
    if i == "B" and len(q) > 0:
        q.pop()

print("".join(q))
