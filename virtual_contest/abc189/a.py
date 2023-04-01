# N, K = map(int, input().split())
S = input()
# W = list(map(str, input().split()))
# AB = [list(map(int, input().split())) for _ in range(N)]

# for i, w in enumerate(S):
#     if w.isupper():
#         print(i+1)
#         break

if S[0] == S[1] and S[1] == S[2] and S[0] == S[2]:
    print("Won")
else:
    print("Lost")
# for w in W:
#     if w in ["and", "not", "that", "the", "you"]:
#         print("Yes")
#         exit()

# print("No")

# print(S.upper())

# print(S.count("v") + S.count("w")*2)
