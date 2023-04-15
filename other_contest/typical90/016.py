# 工夫した全探索、for文を一つ減らす
N = int(input())
A, B , C = map(int, input().split())

max_coin = 9999
c = 2000000000000000000
for i in range(max_coin):
    for j in range(max_coin-i):
        k = (N - A*i - B*j) // C
        if N >= A*i + B*j and (N - A*i - B*j) % C == 0 and N == A*i + B*j + C*k:
            c = min(c, i + j + k)

print(c)
