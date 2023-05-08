N, M = map(int, input().split())
AB = [list(map(int, input().split())) for _ in range(M)]
K = int(input())
CD = [list(map(int, input().split())) for _ in range(K)]

ans = 0
for i in range(2**K):
    d = [0] * (N + 1)
    bin_i = format(i, "b").zfill(K)
    for idx, bit in enumerate(bin_i):
        if bit == "0":
            d[CD[idx][0]] += 1
        if bit == "1":
            d[CD[idx][1]] += 1
    # print(bin_i, d)

    tmp = 0
    for a, b in AB:
        if d[a] >= 1 and d[b] >= 1:
            tmp += 1
    ans = max(ans, tmp)
print(ans)
