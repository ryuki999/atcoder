N = int(input())
A = list(map(int, input().split()))

f = True
for a in A:
    # print(a % 2, a % 3, a % 5)
    if a % 2 == 0:
        if a % 3 == 0 or a % 5 == 0:
            continue
        else:
            f = False

if f:
    print("APPROVED")
else:
    print("DENIED")
