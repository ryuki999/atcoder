X, Y, Z = map(int, input().split())
# S = input()
# T = input()
# A = list(map(int, input().split()))
# A = [i.strip() for i in sys.stdin.readlines()]

dis = 0
if X > 0:
    if Y < 0 or X < Y:
        print(X)
    elif Z > Y:
        print(-1)
    else:
        dis += abs(Z)
        dis += abs(X-Z)
        print(dis)
elif X < 0:
    if Y > 0 or X > Y:
        print(abs(X))
    elif Z < Y:
        print(-1)
    else:
        dis += abs(Z)
        dis += abs(X-Z)
        print(dis)