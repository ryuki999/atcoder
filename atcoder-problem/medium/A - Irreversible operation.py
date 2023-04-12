S = list(input())

count = 0
w_num = 0
for i, s in enumerate(S):
    if s == "W":
        count += (i-w_num)
        w_num += 1

print(count)