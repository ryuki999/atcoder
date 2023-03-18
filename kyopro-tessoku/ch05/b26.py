N = int(input())

MAX = 10**6+1
Deleted = [False for i in range(MAX)]

# エラステネスのふるい
for i in range(2, MAX):
    if Deleted[i]:
        continue
    for j in range(i*2, MAX, i):
        Deleted[j] = True

for i in range(2,N+1):
    if not Deleted[i]:
        print(i)