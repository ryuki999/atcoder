T = int(input())
N = int(input())
LR = [list(map(int, input().split())) for _ in range(N)]

## 別解
# p = [0 for _ in range(T+2)]
# g = [0 for _ in range(T+2)]
# for l, r in LR:
#     p[l] += 1
#     g[r] += -1

# # print(p)
# # print(g)
# ans = 0
# for i in range(T):
#     ans += p[i]
#     ans += g[i]
#     print(ans)



t = [0 for _ in range(T+2)]
for l, r in LR:
    t[l] += 1
    t[r] += -1

# print(p)
# print(g)
ans = 0
for i in range(T):
    ans += t[i]
    print(ans)