import sys

N = int(input())
a = [i.strip() for i in sys.stdin.readlines()]

count = 0
i = 1
while i != 2 and count <= N:
    i = int(a[i-1])
    count += 1

if count > N:
    print(-1)
else:
    print(count)