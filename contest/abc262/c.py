# L1, R1, L2, R2 = map(int, input().split())
N = int(input())
A = list(map(int, input().split()))
# A = [i.strip() for i in sys.stdin.readlines()]

count = 0

c_t = 0
for i in range(N):
    if (i+1) == A[i]:
        c_t += 1
        continue
    if i < A[i]-1 and A[A[i]-1] == (i+1):
        count += 1

ans = c_t * (c_t-1) // 2
ans += count
print(ans)