N, Q = map(int, input().split())
S = input()
LR = [list(map(int, input().split())) for _ in range(Q)]

## 単純な実装(TLE)
# for l, r in LR:
#     t = S[l - 1 : r]
#     if t == t[::-1]:
#         print("Yes")
#     else:
#         print("No")

# 文字を数値に変換（ここでは書籍とは異なり、0-indexed で実装しています）
# ord(c) で文字 c の文字コード（ASCII コード）を取得
T = list(map(lambda c: ord(c) - ord("a") + 1, S))
rev_T = T[::-1]

# 100 の n 乗を前計算
MOD = 2147483647

B = [1] * (N + 1)
for i in range(1, N + 1):
    B[i] = B[i - 1] * 100 % MOD

H = [0] * (N + 1)
rev_H = [0] * (N + 1)
for i in range(1, N + 1):
    H[i] = (H[i - 1] * 100 + T[i - 1]) % MOD
    rev_H[i] = (rev_H[i - 1] * 100 + rev_T[i - 1]) % MOD


# print(T)
# print(B)
# print(H)


# ハッシュ値を求める関数
# S[l-1:r] のハッシュ値は (H[r] - H[l - 1] * power100[r - l + 1]) % MOD で計算
# C++ とは異なり、（負の値）% M (M >= 1) も 0 以上 M-1 以下になることに注意
def hash_value(l, r):
    return (H[r] - H[l - 1] * B[r - l + 1]) % MOD


def rev_hash_value(l, r):
    return (rev_H[r] - rev_H[l - 1] * B[r - l + 1]) % MOD


for l, r in LR:
    # print(T[l:r])
    hash1 = hash_value(l, r)
    # print(rev_T[N - r + 1 : N - l + 1])
    hash2 = rev_hash_value(N - r + 1, N - l + 1)
    # hash2 = rev_hash_value(N - l + 1, N - r + 1)
    if hash1 == hash2:
        print("Yes")
    else:
        print("No")
