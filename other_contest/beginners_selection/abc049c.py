S = input()

tan = ["dream", "dreamer", "erase", "eraser"]
revtan = []
for i in tan:
    revtan.append(i[::-1])

revS = S[::-1]

# print(revtan)
# print(revS)

T = []
t = ""
for i in range(len(revS)):
    t += revS[i]
    for j in revtan:
        # print(t[::-1], j)
        if t == j:
            T.append(j)
            t = ""
            break

# print(revS, T)
if revS == "".join(T):
    print("YES")
else:
    print("NO")
