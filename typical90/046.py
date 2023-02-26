from collections import defaultdict
N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
C = list(map(int, input().split()))

mod_n = 46
a = defaultdict(int)
for i in A:
    a[i % mod_n] +=1
b = defaultdict(int)
for i in B:
    b[i % mod_n] +=1
c = defaultdict(int)
for i in C:
    c[i % mod_n] +=1

ans = 0
for ai, av in a.items():
    for bi, bv in b.items():
        for ci, cv in c.items():
            if (ai + bi + ci) % mod_n == 0:
                ans += av*bv*cv

print(ans)