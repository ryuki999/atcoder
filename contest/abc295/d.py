import copy
import math
from collections import defaultdict

S = input()

# なんで10個？→0~9の数字に対応
cnt = [0] * 10

mp = defaultdict(int)
mp["".join(map(str, cnt))] = 1
for n in S:
    # 各bit位置(数字)の出現回数を数える
    n = int(n)
    cnt[n] += 1
    # 偶数回(2回)出現した場合は0に戻す
    cnt[n] %= 2
    s = "".join(map(str, cnt))
    mp[s] += 1
    # print(n)

# print(mp)

ans = 0
for v in mp.values():
    # nC2個の実装(なぜ？)
    # n個同じRがある時、それらを組み合わせてnC2個の「嬉しい列が」作れるため。
    # 同じRの間の区間の個数と同じ意味を示す。3個の場合は3個作れる。2個の場合は1個つくれる。
    ans += v * (v - 1) // 2
print(ans)
