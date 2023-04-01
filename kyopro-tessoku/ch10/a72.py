from copy import deepcopy

H, W, K = map(int, input().split())
C = [list(input()) for _ in range(H)]


def find_kth_rank_element_index(arr, k):
    sorted_arr = sorted(arr, reverse=True)
    kth_rank_element = sorted_arr[k - 1]
    index = arr.index(kth_rank_element)
    return index


ans = 0
for i in range(2**H):
    h_bin = format(i, "b")[::-1]
    h_1 = h_bin.count("1")
    if h_1 > K:
        continue
    w_1 = max(K - h_1, 0)

    c = deepcopy(C)
    for h_idx, h in enumerate(h_bin):
        if h == "1":
            for w in range(W):
                c[h_idx][w] = "#"

    m = [0] * W
    for w in range(W):
        for hh in range(H):
            if c[hh][w] == ".":
                m[w] += 1

    for j in range(w_1):
        w = find_kth_rank_element_index(m, j + 1)
        for hh in range(H):
            c[hh][w] = "#"

    # print(h_bin)
    # for j in c:
    #     print(j)
    # print()
    count = 0
    for cc in c:
        count += cc.count("#")
    ans = max(ans, count)

print(ans)
