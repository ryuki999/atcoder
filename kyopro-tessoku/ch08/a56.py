N, Q = map(int, input().split())
S = input()
abcd = [list(map(int, input().split())) for _ in range(Q)]

## 単純な実装(TLE)
# for i in range(Q):
#     a, b, c, d = abcd[i]
#     if S[a - 1 : b] == S[c - 1 : d]:
#         print("Yes")
#     else:
#         print("No")

# 文字を数値に変換（ここでは書籍とは異なり、0-indexed で実装しています）
# ord(c) で文字 c の文字コード（ASCII コード）を取得
T = list(map(lambda c: ord(c) - ord("a") + 1, S))

# 100 の n 乗を前計算
MOD = 2147483647

B = [1] * (N + 1)
for i in range(1, N + 1):
    B[i] = B[i - 1] * 100 % MOD
# print(T)
# print(B)

H = [0] * (N + 1)
for i in range(1, N + 1):
    H[i] = (H[i - 1] * 100 + T[i - 1]) % MOD
# print(H)


# ハッシュ値を求める関数
# S[l-1:r] のハッシュ値は (H[r] - H[l - 1] * power100[r - l + 1]) % MOD で計算
# C++ とは異なり、（負の値）% M (M >= 1) も 0 以上 M-1 以下になることに注意
def hash_value(l, r):
    return (H[r] - H[l - 1] * B[r - l + 1]) % MOD


for a, b, c, d in abcd:
    hash1 = hash_value(a, b)
    hash2 = hash_value(c, d)
    if hash1 == hash2:
        print("Yes")
    else:
        print("No")
