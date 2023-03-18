from bisect import bisect, bisect_left, bisect_right

def Get_LISvalue(A):
    L = []
    LEN = 0
    for i in range(N):
        pos = bisect_left(L, A[i])
        # 配列Lを更新
        if pos >= LEN:
            L.append(A[i])
            LEN += 1
        else:
            L[pos] = A[i]
    return LEN
    
N = int(input())
XY = [list(map(int, input().split())) for _ in range(N)]

# ソート
tmp = []
for i in range(N):
	tmp.append([XY[i][0], -XY[i][1]])
tmp.sort()

A = []
for i in range(N):
    A.append(-tmp[i][1])

print(Get_LISvalue(A))