S = input()
N = int(input())

m = []
for i in range(60):
    m.append(2**i)


for idx in range(60):
    if N < m[idx]:
        break
idx -= 1

print(m)
print("idx", idx)
print(S[-idx:].replace("?", "1"))

if "1" in S[:-idx]:
    print(-1)
else:
    print(int(S[-idx:].replace("?", "1"), 2))
