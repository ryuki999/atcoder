# A, B = map(int, input().split())
S = int(input())
# A = list(map(int, input().split()))
# A = [i.strip() for i in sys.stdin.readlines()]

a = hex(S)
if len(a[2:]) == 1:
    print(f"0{a[2:]}".upper())
else:
    print(a[2:].upper())
