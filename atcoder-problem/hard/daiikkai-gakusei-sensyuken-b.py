import numpy as np

N, K = map(int, input().split())
A = list(map(int, input().split()))

# A = np.array(A)
# dp = []

# for i in range(1,K+1):
#     num = 0
#     A = np.array(list(A) * i)
#     for j in range(N):
#         num += sum(A[j+1:] < A[j])
#     dp.append(num)
#     print(A)

# print(dp)

# A = A * K
r = [0]*N
l = [0]*N
mod = 10**9 + 7
for i in range(N):
    for j in range(i+1,N):
        if A[j]<A[i]:
            r[i] += 1
    for j in range(i):
        if A[j]<A[i]:
            l[i] += 1
 
ans = 0
 
for i in range(N):
    ans += r[i]*K*(K+1)//2
    ans %= mod
    ans += l[i]*(K-1)*K//2
    ans %= mod
 
print(ans)