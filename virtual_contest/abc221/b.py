S = input()
T = input()

N = len(S)

a = 0
for i in range(N):
    if S[i] != T[i]:
        a += 1
        continue
    # print(S[i], T[i + 1], S[i + 1], T[i])

if a == 0:
    print("Yes")
elif a == 2:
    for i in range(N - 1):
        if S[i] == T[i]:
            continue
        if S[i] == T[i + 1] and S[i + 1] == T[i]:
            print("Yes")
            exit()
        else:
            print("No")
            exit()
else:
    print("No")
