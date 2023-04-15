N = int(input())
nlen = len(str(N))

ans = 0
# tmp = 0
while nlen > 3:
    # print(N, nlen, ans, tmp)
    if nlen >= 16:
        coef = 5
    elif nlen >= 13 and nlen <= 15:
        coef = 4
    elif nlen >= 10 and nlen <= 12:
        coef = 3
    elif nlen >= 7 and nlen <= 9:
        coef = 2
    elif nlen >= 4 and nlen <= 6:
        coef = 1
    else:
        coef = 0
    tmp = N - int(str(N)[0]) * 10 ** (nlen - 1) + 1
    ans += tmp * coef
    N -= tmp
    nlen = len(str(N))

print(ans)
