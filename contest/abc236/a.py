import copy

S = input()
a, b  = map(int, input().split(" "))

tS = list(copy.copy(S))

tS[a-1] = S[b-1]
tS[b-1] = S[a-1]

print("".join(tS))
