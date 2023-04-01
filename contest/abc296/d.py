N, M = map(int, input().split())

for num in range(M, N*N+1):
    # t = []
    for i in range(1, int(num**(1/2))+1):
        j = num // i
        if j > N:
            continue
        if num % i == 0 and i * j == num:
            # print(f"{n} = {i} * {j}")
            # t.append((i,j))
            print(i*j)
            exit()
print(-1)
