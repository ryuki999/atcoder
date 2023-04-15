"""
ACしたけどちゃんと理解してない
ごちゃごちゃしてる
"""
import bisect
N, K = map(int, input().split())
A = list(map(int, input().split()))

# 累積和をとる
p = [0] * (N + 1)
for i in range(1, N+1):
	p[i] = p[i-1] + A[i-1]

# 配列の準備（R は 0 番目から始まることに注意）
R = [ None ] * N

# しゃくとり法
for i in range(N):
	if i == 0:
		R[i] = -1
	else:
		R[i] = R[i - 1]
	while R[i] < N-1 and p[(R[i]+1)+1] - p[i] <= K:
		R[i] += 1

# 答えを求める
Answer = 0
for i in range(N):
	Answer += (R[i] - i + 1)
print(Answer)