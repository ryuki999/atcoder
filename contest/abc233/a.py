X, Y = map(int, input().split(" "))

count = 0
while X < Y:
    X += 10
    count += 1
    # if X > Y:
    #     count -= 1

print(count)
