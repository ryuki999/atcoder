import sys
from collections import defaultdict

N = int(input())
A = [int(i.strip()) for i in sys.stdin.readlines()]

memo = defaultdict(int)
for i in A:
    memo[i] += 1

count = 0
for i, v in memo.items():
    if v % 2 != 0:
        count += 1
print(count)