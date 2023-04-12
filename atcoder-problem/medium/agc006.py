N = int(input())
s = input()
t = input()

for i in range(N):
    if s[i:] == t[: N - i]:
        print(i + N)
        exit()

print(N * 2)
