from collections import defaultdict

H, W = map(int, input().split())
A = [list(input()) for _ in range(H)]
B = [list(input()) for _ in range(H)]

for i in range(31):
    A.append(A[0])
    A.pop(0)
    for _ in range(31):
        for j in range(H):
            A[j].append(A[j][0])
            A[j].pop(0)

        flag = True
        for k in range(H):
            for l in range(W):
                if A[k][l] != B[k][l]:
                    flag = False

        if flag:
            print("Yes")
            exit()

            # print(i, j)
            # for a in A:
            #     print(a)
            # print()

print("No")
