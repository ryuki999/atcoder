A, B = map(int, input().split())

ans = 1
c = 0
while True:
    if ans >= B:
        break
    ans += A - 1
    c += 1

print(c)
