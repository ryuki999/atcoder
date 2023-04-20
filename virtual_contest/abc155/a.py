from collections import defaultdict

A, B, C = map(int, input().split())
# S = input()
# W = list(map(str, input().split()))
# AB = [list(map(int, input().split())) for _ in range(N)]

if A == B and A != C:
    print("Yes")
elif A == C and A != B:
    print("Yes")
elif B == C and A != C:
    print("Yes")
else:
    print("No")
