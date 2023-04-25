N = list(map(str, list(input())))

ans = 0
for i in range(2 ** len(N)):
    bin_i = format(i, "b")
    if len(bin_i) < len(N) or "0" not in bin_i or "1" not in bin_i:
        continue
    front = []
    back = []
    for idx, v in enumerate(bin_i):
        if v == "0":
            front.append(N[idx])
        if v == "1":
            back.append(N[idx])
    front = sorted(front, reverse=True)
    back = sorted(back, reverse=True)
    # print(front, back)
    front_num = int("".join(front))
    back_num = int("".join(back))
    ans = max(ans, front_num * back_num)

print(ans)
