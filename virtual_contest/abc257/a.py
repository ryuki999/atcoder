N, X = map(int, input().split())
# S = input()
# W = list(map(str, input().split()))
# AB = [list(map(int, input().split())) for _ in range(N)]

a = ""
for i in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
    a += i * N

print(a[X - 1])
