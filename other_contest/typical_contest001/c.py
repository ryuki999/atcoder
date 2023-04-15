N = int(input())
AB = [list(map(int, input().split())) for _ in range(N)]

for k in range(1, 2 * N + 1):
    ans = 0
    for i in range(1, k):
        # k = k % N
        # if k == AB[i - 1][0] * AB[k - i - 1][1]
        if k - i <= 0 or k - i >= N:
            continue
        print(k, i - 1, k - i - 1, AB[i - 1][0] * AB[k - i - 1][1])
        # if k > N:
        #     ans += AB[i - 1][0] * AB[k - i - 1][1] * 2
        # else:
        # ans += AB[i - 1][0] * AB[k - i - 1][1]
        ans += AB[i - 1][0] * AB[k - i - 1][1]
        # if i == k - i:
        #     ans += AB[i - 1][0] * AB[k - i - 1][1]
        # elif i < k - i:
        #     ans += AB[i - 1][0] * AB[k - i - 1][1]
        # else:
        #     ans += AB[i - 1][1] * AB[k - i - 1][0]
        # print(ans)
    print(ans)
