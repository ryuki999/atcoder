from collections import defaultdict

S = input()
N = len(S)

# final = [0] * len(S)
# for i in range(len(S)):
#     pos = i
#     if S[pos] == "R" and S[pos + 1] == "L":
#         final[pos] += 1
#         continue
#     elif S[pos] == "L" and S[pos - 1] == "R":
#         final[pos] += 1
#         continue
#     else:
#         count = 0
#         if S[pos] == "R":
#             while S[pos + 1] != "L":
#                 count += 1
#                 pos += 1
#             if count % 2 != 0:
#                 pos += 1

#         elif S[pos] == "L":
#             while S[pos - 1] != "R":
#                 count += 1
#                 pos -= 1
#             if (count) % 2 != 0:
#                 pos -= 1
#         final[pos] += 1

# print(*final)

# ダブリング(https://blog.hamayanhamayan.com/entry/2019/08/07/204315)
dp = [[0] * N for _ in range(33)]
ans = [0] * N

# p=0,1回目の移動。2^pずつ位置を確認する。
for i in range(N):
    if S[i] == "R":
        dp[0][i] = i + 1
    else:
        dp[0][i] = i - 1

# p=1以降の移動。
for p in range(32):
    for i in range(N):
        dp[p + 1][i] = dp[p][dp[p][i]]

# for i in dp:
#     print(i)

# ansに要素の個数をカウントして格納
for i in range(N):
    ans[dp[32][i]] += 1

print(*ans)
