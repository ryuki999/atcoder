def main():
    L, N1, N2 = map(int, input().split())
    compressed_row1 = [tuple(map(int, input().split())) for _ in range(N1)]
    compressed_row2 = [tuple(map(int, input().split())) for _ in range(N2)]

    count = 0
    i1 = i2 = 0
    l1 = l2 = 0
    while i1 < N1 and i2 < N2:
        v1, len1 = compressed_row1[i1]
        v2, len2 = compressed_row2[i2]

        min_len = min(len1 - l1, len2 - l2)
        if v1 == v2 and l1 == l2:
            count += min_len

        if len1 - l1 > len2 - l2:
            l1 += min_len
            i2 += 1
            l2 = 0
        elif len1 - l1 < len2 - l2:
            l2 += min_len
            i1 += 1
            l1 = 0
        else:
            l1 = l2 = 0
            i1 += 1
            i2 += 1

    print(count)

if __name__ == "__main__":
    main()
