X, Y = map(int, input().split())

ans = 0
process = []

while X != Y:
    process.append((X, Y))
    if X >= Y:
        X -= Y
    else:
        Y -= X
    ans += 1

print(ans)
for i in process[::-1]:
    print(*i)
