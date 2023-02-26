t = int(input())

def fx(x):
    return x**2+2*x+3
    
y = fx(fx(fx(t) + t) + fx(fx(t)))

print(y)
