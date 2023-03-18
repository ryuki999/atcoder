Q = int(input())
X = [int(input()) for _ in range(Q)]

# √nの約数だけ判定する方法
# for i in range(Q):
#     f = True
#     for j in range(2, int(X[i]**0.5)+1):
#         if X[i] % j == 0:
#             f = False

#     if f:
#         print("Yes")
#     else:
#         print("No")

N = 300001
Deleted = [False for i in range(N+1)]

# エラステネスのふるい
for i in range(2, N+1):
    if Deleted[i]:
        continue
    for j in range(i*2, N+1, i):
        Deleted[j] = True

for i in range(Q):
    if Deleted[X[i]]:
        print("No")
    else:
        print("Yes")