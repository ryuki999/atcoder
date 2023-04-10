from collections import defaultdict

N =int(input())
a = list(map(int, input().split()))

num_dic = defaultdict(int)

for i in range(N):
    num_dic[a[i]-1] += 1
    num_dic[a[i]] += 1 
    num_dic[a[i]+1] += 1

# print(num_dic)
print(max(num_dic.values()))