# N, K = map(int, input().split())
S = input()
# A = list(map(int, input().split()))
# A = [i.strip() for i in sys.stdin.readlines()]

# if K < N:
#     A = A[K:] + [0]*K
# else:
#     A = A[K:] + [0]*N

# print(*A)

print(S.count("v") + S.count("w")*2)
