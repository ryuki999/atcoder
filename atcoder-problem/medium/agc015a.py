N, A, B = map(int, input().split())

max_n = A + B*(N-1)
min_n = A*(N-1) + B

ans = max_n-min_n+1
if ans < 0:
    ans =0

print(ans)