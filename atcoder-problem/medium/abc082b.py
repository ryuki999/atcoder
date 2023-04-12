s = input()
t = input()

t = sorted(t, reverse=True)
s = sorted(s)
# print(t)
if t > s:
    print("Yes")
else:
    print("No")
