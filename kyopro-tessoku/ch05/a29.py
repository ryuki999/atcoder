a, b = map(int, input().split())

MOD = 10**9+7

def POW(a, b):
    ans = 1
    for i in range(30):
        if (b // 2**i) % 2 == 1:
            ans = (ans * a) % MOD
        
        a = (a*a) % MOD
    return ans
# t = 1
# for i in range(b):
#     t = (t * a) % MOD

# 23(10111)なので、bを2**iで割った余が1のものだけ乗算する


print(POW(a, b))
# print(a, b)