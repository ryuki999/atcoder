from collections import defaultdict

S = input()
T = input()

sd = defaultdict(int)
td = defaultdict(int)

for i, j in zip(S, T):
    sd[i] += 1
    td[j] += 1

# print(sd)
# print(td)

for i in ["a", "t", "c", "o", "d", "e", "r"]:
    # if i in sd or i in td:
    #     print(i, sd[i] - td[i])
    if sd[i] - td[i] < 0:
        if sd["@"] >= abs(sd[i] - td[i]):
            sd["@"] -= abs(sd[i] - td[i])
            sd[i] += abs(sd[i] - td[i])
        else:
            print("No")
            exit()
    if sd[i] - td[i] > 0:
        if td["@"] >= abs(sd[i] - td[i]):
            td["@"] -= abs(sd[i] - td[i])
            td[i] += abs(sd[i] - td[i])
        else:
            print("No")
            exit()
    # print(sd)
    # print(td)

if "@" not in sd:
    sd["@"] = 0
if "@" not in td:
    td["@"] = 0

if sd == td:
    print("Yes")
else:
    print("No")

# print(sd)
# print(td)
