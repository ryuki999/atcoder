N, K = map(int, input().split())
AB = [tuple(map(int, input().split())) for _ in range(N)]

ans = 0
for a in range(1, 101):
    for b in range(1, 101):
        tmp = 0
        for i in range(N):
            if (
                a <= AB[i][0]
                and AB[i][0] <= a + K
                and b <= AB[i][1]
                and AB[i][1] <= b + K
            ):
                # if (a + K, b + K) >= AB[i] and (a, b) <= AB[i]:
                tmp += 1
        ans = max(ans, tmp)

print(ans)
