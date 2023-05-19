N, M = map(int, input().split())
PS = [list(input().split()) for _ in range(M)]

ac = [0] * (N + 1)
wa = [0] * (N + 1)
for p, s in PS:
    if s == "WA" and ac[int(p)] <= 0:
        wa[int(p)] += 1
    if s == "AC":
        ac[int(p)] += 1

ac_n = 0
wa_n = 0
for i in range(1, N + 1):
    if ac[i] > 0:
        ac_n += 1
        wa_n += wa[i]
print(ac_n, wa_n)
