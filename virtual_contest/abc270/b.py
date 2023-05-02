import math

X, Y, Z = map(int, input().split())


print(X)
if abs(Y) > abs(X):
    print(X)
else:
    if abs(Z) > abs(Y):
        print(-1)
        exit()
    if abs(Z) < abs(Y):
        if Z > 0:
            print(X)
        if Z < 0:
            print(X + 2 * abs(Z))
