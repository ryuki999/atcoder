N, K = map(int, input().split())
# S = input()
A = list(map(int, input().split()))
# A = [i.strip() for i in sys.stdin.readlines()]

# if S.find("a") == -1:
#     print(-1)
# else:
#     print(S.rfind('a') + 1)

if K < N:
    A = A[K:] + [0]*K
else:
    A = A[K:] + [0]*N

print(*A)
