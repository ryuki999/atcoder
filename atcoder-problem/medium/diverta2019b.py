R, G, B, N = map(int, input().split())

count = 0

for i in range(N+1):
    for j in range(N+1):
        if N >= (R * i + G * j) and (N - R * i - G * j) % B == 0:
            count += 1
            # print(R * i, G * j)

print(count)
