# import copy
# N, K = map(int, input().split())

# mod = 10**9 + 7

# def binpower(a, b):
#     ans = 1
#     m = copy.copy(a)
#     while b != 0:
#         print(b)
#         if b % 2 == 1:
#             ans = ans * m % mod
#         m = m * a % mod
#         b = b // 2
    
#     return ans

# if K == 1:
#     if N == 1:
#         ans = 1
#     else:
#         ans = 0
# elif N == 1:
#     ans = K % mod
# elif N == 2:
#     ans = K * (K - 1) % mod
# else:
#     ans = (K * (K - 1) % mod) * (binpower(K-2, N-2) % mod)

# print(ans % mod)

        

N, K = map(int,input().split())
mod = 10 ** 9 + 7
if N == 1:
    print(K)
else:
    ans = K * (K - 1) * pow(K - 2, N - 2, mod)
    print(ans % mod)