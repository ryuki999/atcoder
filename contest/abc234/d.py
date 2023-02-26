N, K = map(int, input().split(" "))
P = list(map(int, input().split(" ")))

def cal_max(array):
    pre_num = sorted(array)[-(K-1)]
    num = sorted(array)[-K]
    # post_num = sorted(array)[-(K+1)]
    return pre_num, num
    # return pre_num, num, post_num

pre_num, num = cal_max(P[:K])
# pre_num, num, post_num = cal_max(P[:K])
print(num)

for i in range(0,N-K):

    if pre_num < P[K+i]:
        pre_num, num = cal_max(P[:K+i+1])
        print(num)
    else:
        print(num)

