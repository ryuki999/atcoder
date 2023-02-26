import sys

N = int(input())
S = [int(i.strip()) for i in sys.stdin.readlines()]

max_sum = sum(S)

if max_sum % 10 != 0:
    print(max_sum)
else:
    S.sort()
    for i in S:
        if i % 10 != 0:
            print(max_sum-i)
            exit()
    
    print(0)
