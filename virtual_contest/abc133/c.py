L, R = map(int, input().split())

mini = 10**26
for i in range(L, R + 1):
    for j in range(i + 1, R + 1):
        if j % 2019 == 0:
            print(0)
            exit()
        mini = min(mini, i % 2019 * j % 2019) % 2019

print(mini)
