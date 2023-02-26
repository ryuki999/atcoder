A, B, C = map(int, input().split())

count = 1
a = 0
for i in range(1, B+1):
    a = A * i
    if a % B == C:
        print("YES")
        exit()
print("NO")