N, A, B = map(int, input().split())
# N = int(input())
# S = input()
C = list(map(int, input().split()))
# AB = [list(map(int, input().split())) for _ in range(N)]

print(C.index(A + B) + 1)
