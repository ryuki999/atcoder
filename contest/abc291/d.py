"""
未AC
理由：分からないから
"""
import copy
import math
from collections import defaultdict

N = int(input())

AB = [list(map(int, input().split())) for i in range(N)]

MOD=998244353

dp = [[0,0] for _ in range(N)]
dp[0] = [1,1]
for i in range(1,N):
  # 配るDP
  for pre in range(2):
    for nxt in range(2):
      if AB[i-1][pre] != AB[i][nxt]:
        dp[i][nxt] += dp[i-1][pre]
  dp[i][0] %= MOD
  dp[i][1] %= MOD
print((dp[N][0]+dp[N][1]) % MOD)