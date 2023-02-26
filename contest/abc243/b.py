N = int(input())
A = list(map(int, input().split(" ")))
B = list(map(int, input().split(" ")))

top = 0
for i in range(0, N):
    if A[i] == B[i]:
        top += 1

count = 0
for i in range(0, N):
    if A[i] in B and A[i] != B[i]:
        count += 1

# bottom = len(A)-count-top

print(top)
print(count)
