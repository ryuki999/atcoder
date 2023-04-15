N, M = map(int, input().split())

while M > 1:
    if (N + 1) * 2 > M - 2:
        break
    M -= 2
    N += 1
print(N)
