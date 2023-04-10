N = int(input())
S = input()

max = 0
for i in range(N):
    left = {}
    right = {}
    for j in range(0,i):
        left[S[j]] = 1
    for j in range(i,N):
        right[S[j]] = 1
    
    if max < len(set(left.keys()) & set(right.keys())):
        max = len(set(left.keys()) & set(right.keys()))

    # print(set(left.keys()) & set(right.keys()))
print(max)