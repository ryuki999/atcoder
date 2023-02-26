K = int(input())

num = str(bin(K)[2:])
num = num.replace("1", "2")

print(num)
