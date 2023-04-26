H = int(input())

i = 0
ans = 0
while H > 0:
    ans += 2**i
    # print(H)
    H //= 2
    i += 1
print(ans)
