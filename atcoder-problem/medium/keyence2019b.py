S = input()

N = len(S)

flag = False
index = N

for i in range(N):
    for j in range(i, N):
        if S[:i] + S[j:] == "keyence":
            flag =True
            break

if flag:
    print("YES")
else:
    print("NO")