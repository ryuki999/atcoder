import sys

N = int(input())
A = list(map(int, input().split(" ")))

 
unique_a = sorted(list(set(A)), reverse=True)

pre_c = "".join([str(i) for i in A if i != unique_a[0]])
for u in unique_a[1:]:
    c = "".join([str(i) for i in A if i != u])
    if c >= pre_c:
        break
    else:
        pre_c = c

print((" ".join(list(pre_c))))
