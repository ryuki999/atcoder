N = int(input())
A = list(map(int, input().split()))

a0 = 0
a1 = 0
a4 = 0
for a in A:
    if a % 4 == 0:
        a4 += 1
    elif a % 2 == 0:
        a1 += 1
    elif a % 2 == 1:
        a0 += 1

# print(a0, a1, a4)
# 自分の解
# if N % 2 == 0:
#     if a0 <= a4 and a1 % 2 == 0:
#         print("Yes")
#     else:
#         print("No")
# else:
#     if a0 - 1 <= a4 and (a1 == 0 or a1 % 2 == 1):
#         print("Yes")
#     else:
#         print("No")

# 解説解
if a1 > 0:
    a0 += 1

if a0 - 1 <= a4:
    print("Yes")
else:
    print("No")
