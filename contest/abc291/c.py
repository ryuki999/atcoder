import copy
from collections import defaultdict

N = int(input())
S = input()

cor = [0,0]
cors = defaultdict(int)
cors[f"0,0"] += 1
for i in range(N):
    if S[i] == "R":
        cor[0] += 1
    if S[i] == "L":
        cor[0] -= 1
    if S[i] == "U":
        cor[1] += 1
    if S[i] == "D":
        cor[1] -= 1
    cors[f"{cor[0]},{cor[1]}"] += 1
    # print(f"{cor[0]},{cor[1]}")

# print(cors)

for i, v in cors.items():
    if v > 1:
        print("Yes")
        exit()

print("No")