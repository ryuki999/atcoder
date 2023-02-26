N, K = map(int, input().split(" "))
A = list(map(int, input().split(" ")))

def get_integral_value_combination(list, target):
    def a(idx, l, r, t):
        if t == sum(l): r.append(l)
        elif t < sum(l): return
        for u in range(idx, len(list)):
            a((u + 1), l + [list[u]], r, t)
        return r
    return a(0, [], [], target)

if len(get_integral_value_combination(A, K)) is None:
    print(0)
else:
    print(len(get_integral_value_combination(A, K)))
