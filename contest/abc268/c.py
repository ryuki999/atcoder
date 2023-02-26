N = int(input())
P = list(map(int, input().split()))

# c = 0
# for i in range(N):
#   count = 0
#   for j in range(N):
#     index = (j + i) % N
#     if P[index] == (j-1) % N or j == P[index] or P[index] == (j+1) % N:
#       count += 1
#   c = max(c, count)

# print(c)

c = [0 for _ in range(N)]

for j in range(N):
    c[(P[j] - (j + 1)) % N] += 1
    c[(P[j] - j) % N] += 1
    c[(P[j] - (j - 1)) % N] += 1

print(max(c))