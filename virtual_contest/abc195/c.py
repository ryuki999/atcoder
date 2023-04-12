N = int(input())

nlen = len(str(N))

ans = 0
while nlen > 3:
    print(N,nlen, ans )    
    if nlen >= 13 and nlen <= 15:
        coef = 4
    elif nlen >= 10 and nlen <= 12:
        coef = 3
    elif nlen >= 7 and nlen <= 9:
        coef = 2
    elif nlen >= 4 and nlen <= 6:
        coef = 1
    
    a = int(str(N)[0]) * 10**(nlen-1)
    ans += (N - a+1)*coef
    print(a, (N - a+1))
    N -= a
    nlen = len(str(N))

print(ans)