import sys

N, X = map(int, input().split())
AB = [list(map(int, i.strip().split())) for i in sys.stdin.readlines()]

ans = 10**20
sum = 0
m = 10**20
for i in range(1, N+1):
    sum += AB[i-1][0] + AB[i-1][1]
    m = min(m, AB[i-1][1])
    tmp = sum + m*(X-i)
    ans = min(ans, tmp)

# print(m)
print(ans)