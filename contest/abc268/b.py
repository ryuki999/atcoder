# N, M = map(int, input().split())
S = input()
T = input()
# A = list(map(int, input().split()))
# A = [i.strip() for i in sys.stdin.readlines()]

# print(T[:len(S)])
# print(S)
f = S == T[:len(S)]
if f:
    print("Yes")
else:
    print("No")
# print(f)