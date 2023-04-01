from copy import copy, deepcopy

H, W, K = map(int, input().split())
C = [list(input()) for _ in range(H)]

ans = 0
for i in range(2**H):
    h_bin = format(i, "b")[::-1]
    for j in range(2**W):
        w_bin = format(j, "b")[::-1]
        c = deepcopy(C)
        # print(h_bin, w_bin)

        for h_idx, h in enumerate(h_bin):
            if h == "1":
                for k in range(W):
                    c[h_idx][k] = "."
        for w_idx, w in enumerate(w_bin):
            if w == "1":
                for k in range(H):
                    c[k][w_idx] = "."

        count = 0
        for cc in c:
            # print(cc)
            count += cc.count("#")
        if count == K:
            ans += 1

print(ans)
