"""
理解していないので未AC
"""
N = int(input())

Power10 = [None] * 17
for i in range(17):
    Power10[i] = 10**i

# R[i][j] の値を計算
R = [[None] * 10 for i in range(17)]
for i in range(16):
    # 下から i 桁目の数字を求める
    Digit = (N // Power10[i]) % 10

    # R[i][j] の値を求める
    for j in range(10):
        if j < Digit:
            R[i][j] = (N // Power10[i + 1] + 1) * Power10[i]
        if j == Digit:
            R[i][j] = (N // Power10[i + 1]) * Power10[i] + (N % Power10[i]) + 1
        if j > Digit:
            R[i][j] = (N // Power10[i + 1]) * Power10[i]


ans = 0
for i in range(16):
    for j in range(10):
        ans += j * R[i][j]

print(ans)
