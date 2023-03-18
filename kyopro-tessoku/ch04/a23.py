N, M = map(int, input().split())

# A = [list(input().split()) for _ in range(M)]
A = [list(map(int, input().split())) for _ in range(M)]

MAX = 10**9
dp = [[MAX] * (2**N) for _ in range(M+1)]
dp[0][0] = 0

for i in range(M):
    for j in range(2**N):
        # 配列の添字をビットで表す
        # 1が立ってるところは候補
        # already = [None] * N
        # for k in range(N):
        #     if (j // (2**k)) % 2 == 0:
        #         already[k] = 0
        #     else:
        #         already[k] = 1
        
        already = format(j, "b").zfill(N)[::-1]
        # print(already)

        v = 0
        for k in range(N):
            if already[k] == "1" or A[i][k] == 1:
                v += (2**k)
        
        dp[i+1][j] = min(dp[i+1][j], dp[i][j])
        dp[i+1][v] = min(dp[i+1][v], dp[i][j]+1)

# print(dp)
# for i in dp:
#     print(i)

if dp[M][2**N-1] == MAX:
    print(-1)
else:
    print(dp[M][2**N-1])
