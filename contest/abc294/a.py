# N, K = map(int, input().split())
S = int(input())
A = list(map(int, input().split()))
# AB = [list(map(int, input().split())) for _ in range(N)]

# for i, w in enumerate(S):
#     if w.isupper():
#         print(i+1)
#         break

for i in A:
    if i % 2 == 0:
        print(i, end=" ")
print()
# print(S.upper())

# print(S.count("v") + S.count("w")*2)
