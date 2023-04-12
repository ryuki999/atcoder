A, B, W = map(int, input().split())

ans = 0
for i in range(A,B+1):
    for c in range(10**2):
        if i*c > W*1000:
            