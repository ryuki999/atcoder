import numpy as np

N = int(input())

print(N*(N-1) // 2)

# n = [i+1 for i in range(N)]

# p = n[1:]
# p.append(1)

# print(np.array(n) % np.array(p))

# sum = 0
# for i, j in zip(n,p):
#     sum += i % j
# print(n, p, sum)