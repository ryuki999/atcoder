n = int(input())
A = list(map(int, input().split()))

ans = 0
for i in range(1, n - 1):
    c = 0
    if A[i] <= A[i - 1]:
        c += 1
    if A[i] <= A[i + 1]:
        c += 1
    if c == 1:
        ans += 1

print(ans)
