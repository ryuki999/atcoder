N = int(input())

ans = (N // 500) * 1000
N -= 500 * (N // 500)
# print(N, ans)
ans += (N // 5) * 5
# print(N, ans)
# N -= 5 * (N // 5)

print(ans)
