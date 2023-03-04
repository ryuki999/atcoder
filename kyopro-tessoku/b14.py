import bisect
N, K = map(int, input().split())

A = list(map(int, input().split()))

M = N//2
front_A = A[:M]
back_A = A[M:]

def array_comnbination_total(l):
    P = []
    M = len(l)
    for i in range(2**M):
        t = 0
        for j, bit in enumerate(bin(i)[2:][::-1]):
            if bit == "1":
                t += l[j]
        # print(bin(i)[2:][::-1], t)
        P += [t]
    # return P
    return list(set(P))

P = array_comnbination_total(front_A)
Q = array_comnbination_total(back_A)

P.sort()
Q.sort()
# print(P, Q)

# 二分探索モジュール版
# for p in P:
#     pos = bisect.bisect_left(Q, K-p)
#     if pos < len(Q) and Q[pos] == K-p:
#         print("Yes")
#         exit()
# print("No")

# 二分探索自作版
for p in P:
    L = 0
    R = len(Q)
    while L < R:
        M = (L + R) // 2
        if K - p < Q[M]:
            R = M
        if K - p > Q[M]:
            L = M + 1
        if K - p == Q[M]:
            print("Yes")
            exit()
print("No")