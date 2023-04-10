s = input()
 
a = [0 for i in range(len(s) + 1)]
 
if s[0] == '<':
    a[1] = 1
for i in range(1, len(a)-1):
    if s[i] == '<':
        a[i+1] = a[i] + 1
 
if s[-1] == '>':
    a[-2] = max(1, a[-2])
for i in range(1, len(a)-1):
    ind = -(i+1)
    if s[ind] == '>':
        a[ind-1] = max(a[ind] + 1, a[ind-1])
 
print(sum(a))