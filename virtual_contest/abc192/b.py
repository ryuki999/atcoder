S = input()

ans = True
for i in range(len(S)):
    if (i+1) % 2 == 1:
        # print(S[i], S[i].islower())
        if not S[i].islower():
            ans = False
            break
    if (i+1) % 2 == 0:
        # print(S[i], S[i].isupper())
        if not S[i].isupper():
            ans = False
            break

if ans:
    print("Yes")
else:
    print("No")
