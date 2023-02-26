# N = int(input())
N, L, R = map(int, input().split())
A = list(map(int, input().split()))
# CY = [list(map(int, input().split())) for i in range(M)]

dp = []


for x in range(N):
    for y in range(N):