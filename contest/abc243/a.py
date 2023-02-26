V, A, B, C  = map(int, input().split(" "))

while V > 0:
    V -= A
    if V < 0:
        print("F")
        exit()

    if V == 0:
        print("M")
        exit()
    V -= B
    if V < 0:
        print("M")
        exit()

    if V == 0:
        print("T")  
        exit()
    V -= C
    if V < 0:
        print("T")
        exit()
    if V == 0:
        print("F")  
        exit()
