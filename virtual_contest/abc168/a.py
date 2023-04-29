# N, A, B = map(int, input().split())
N = input()
# W = list(map(str, input().split()))
# AB = [list(map(int, input().split())) for _ in range(N)]

if N[-1] in ["2", "4", "5", "7", "9"]:
    print("hon")
if N[-1] in ["0", "1", "6", "8"]:
    print("pon")
if N[-1] in ["3"]:
    print("bon")
