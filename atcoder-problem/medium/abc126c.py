N, K = map(int, input().split())

prob = 0
total = 0
for i in range(1,N+1):
    if i < K:
        num = i
        count = 0
        for _ in range(K):
            num *= 2
            count += 1
            if  num >= K:
                # print(count, end=" ")
                break
        prob += (1/N) * ((1/2)**count)    
    else:
        total += 1
prob += total/N
print(prob)