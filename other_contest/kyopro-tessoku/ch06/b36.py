N, K = map(int, input().split())
S = input()

c = S.count("1")
if c % 2 == K % 2:
    print("Yes")
else:
    print("No")
