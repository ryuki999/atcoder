N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

A = sorted(A)
B = sorted(B, reverse=True)

ans = 0
for a, b in zip(A, B):
    ans += a * b

print(ans)
