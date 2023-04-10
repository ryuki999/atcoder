import sys

C = [list(map(int, i.strip().split())) for i in sys.stdin.readlines()]

for a1 in range(100):
    b1 = C[0][0] - a1
    b2 = C[0][1] - a1
    b3 = C[0][2] - a1
    a2 = C[1][0] - b1
    a3 = C[2][2] - b3

    # print(a1, a2, a3, b1, b2, b3)
    if (a1 + b1) == C[0][0] and (a1 + b2) == C[0][1] and (a1 + b3) == C[0][2]:
        if (a2 + b1) == C[1][0] and (a2 + b2) == C[1][1] and (a2 + b3) == C[1][2]:
            if (a3 + b1) == C[2][0] and (a3 + b2) == C[2][1] and (a3 + b3) == C[2][2]:
                print("Yes")
                exit()
print("No")