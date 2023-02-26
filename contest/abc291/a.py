# N, K = map(int, input().split())
S = input()
# A = list(map(int, input().split()))
# A = [i.strip() for i in sys.stdin.readlines()]

for i, w in enumerate(S):
    if w.isupper():
        print(i+1)
        break


# print(S.count("v") + S.count("w")*2)
