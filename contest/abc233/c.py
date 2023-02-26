import sys

import numpy as np

inputs = sys.stdin.readlines()

# print(inputs)
N, X = map(int, inputs[0].strip().split(" "))

array = []
max_index = []
for i in inputs[1:]:
    max_index.append(list(map(int, i.strip().split(" ")))[0])
    array.append(list(map(int, i.strip().split(" ")))[1:])
# print(max_index)
# print(array)

index = [0 for _ in range(0, N)]
num_sum = []

max_num = 1
for i in max_index:
    max_num *= i

# print(max_num)

for num in range(0, max_num):
    count = 0
    sum_ = 1
    for i in index:
        # print(count, i)
        sum_ *= array[count][i]
        count += 1
    
    num_sum.append(sum_)
    # print(num_sum)

    for i in range(0, N):
        if index[i] < max_index[i]-1:
            index[i] += 1
            break
        else:
            index[i] = 0
            
    # print(index)


print(sum(np.array(num_sum) == X))
