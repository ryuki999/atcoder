N = int(input())
S = input()

# 最後の状態を考えると、必ずBBBかRRRが存在する
if "BBB" in S or "RRR" in S:
    print("Yes")
else:
    print("No")
