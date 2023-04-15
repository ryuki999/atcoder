N, C = input().split()
A = input()

t = 0
for i in range(int(N)):
    if A[i] == "W":
        t += 0
    if A[i] == "B":
        t += 2
    if A[i] == "R":
        t += 1
if t % 3 == 0 and C == "W":
    print("Yes")
elif t % 3 == 1 and C == "R":
    print("Yes")
elif t % 3 == 2 and C == "B":
    print("Yes")
else:
    print("No")
