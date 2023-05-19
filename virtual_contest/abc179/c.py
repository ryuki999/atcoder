N = int(input())

ans = 0
for a in range(1, N):
    # Nのaに対する約数の個数を調べる
    # N=100のとき、a=100の場合はないので、-1する
    ans += (N - 1) // a

print(ans)
