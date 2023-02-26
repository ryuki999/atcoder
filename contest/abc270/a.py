A, B = map(int, input().split())
# S = input()
# A = list(map(int, input().split()))
# A = [i.strip() for i in sys.stdin.readlines()]

t = {
    1:[1],
    2:[2],
    4:[4],
    3:[1,2],
    5:[1,4],
    6:[2,4],
    7:[1,2,4]
    }

a = []
for i, v in t.items():
    if i == A:
        a += t[A]

for i, v in t.items():
    if i == B:
        a += t[B]

print(sum(set(a)))