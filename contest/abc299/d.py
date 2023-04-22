from bisect import bisect_left, bisect_right

# N = input()

N = int(input())
d = [-1] * (N)
d[0] = 0
d[N - 1] = 1

R = N - 1
L = 0
# M = (L + R) // 2

for i in range(1, 21):
    M = (L + R) // 2
    print(f"? {M+1}")
    # ans = int(input())

    # print(A[M])]
    O = int(input())
    d[M] = O
    if O == 1:
        R = M - 1
    if O == 0:
        L = M + 1

for i in range(N - 1):
    if d[i] == 0 and d[i + 1] == 1:
        print(f"! {i+1}")
        exit()
    if d[i] == 1 and d[i + 1] == 0:
        print(f"! {i+1}")
        exit()


# print(M + 1)
