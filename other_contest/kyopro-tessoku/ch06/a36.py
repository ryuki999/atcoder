N, K = map(int, input().split())

min_tekazu = (N - 1) * 2
if min_tekazu <= K and K % 2 == 0:
    print("Yes")
else:
    print("No")
