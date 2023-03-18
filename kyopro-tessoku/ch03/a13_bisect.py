import bisect
N, K = map(int, input().split())
A = list(map(int, input().split()))

sum_ = 0
for i in range(N):
    # 一致しているものも含めた左への要素数
    Ri = bisect.bisect(A, abs(A[i]+K))
    # 一致しているものは除外したものから左への要素数
    # Ri = bisect.bisect_left(A, abs(A[i]+K))
    sum_ += (Ri - i - 1)

print(sum_)