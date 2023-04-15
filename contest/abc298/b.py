import copy

N = int(input())
A = [list(map(int, input().split())) for _ in range(N)]
B = [list(map(int, input().split())) for _ in range(N)]

for _ in range(4):
    ans =[['']*N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            ans[j][N-1-i] = A[i][j]
    A = copy.copy(ans)
    flag = True
    for i in range(N):
        for j in range(N):
            if A[i][j] ==1:
                if B[i][j]==1:
                    continue
                else:
                    flag=False
            else:
                continue

    if flag:
        print("Yes")
        exit()

    # for i in ans:
    #     print(i) 
    # print()   
print("No")
