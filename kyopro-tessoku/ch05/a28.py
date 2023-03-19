N = int(input())
TA = [list(input().split()) for _ in range(N)]

t = 0
for i in range(N):
    if TA[i][0] == "+":
        t += int(TA[i][1])
    if TA[i][0] == "*":
        t *= int(TA[i][1])
    if TA[i][0] == "-":
        t -= int(TA[i][1])
    if t < 0:
        t += 10000
    t %= 10000

    print(t%10000)