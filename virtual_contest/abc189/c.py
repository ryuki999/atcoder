N = int(input())
A = list(map(int, input().split()))

ans = 0
for l in range(N):
    # 最初は左端の値を下限にする
    th = A[l]
    for r in range(l, N):
        # 右にあるものと比較して下限を更新する
        th = min(th, A[r])
        ans = max(ans, th * (r - l + 1))

print(ans)
