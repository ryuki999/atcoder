# import itertools
k = [3, 5, 7]
# comb = itertools.combinations(k, 2)
comb = [(3,5), (3,7), (5,7)]
N = int(input())

ans = N//3 + N//5 + N//7

for i, j in comb:
    ans -= N//(i*j)

ans += N//(3*5*7)
print(ans)