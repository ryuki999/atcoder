N, M = map(int, input().split())
# N = int(input())
# A = list(map(int, input().split()))
# A = [i.strip() for i in sys.stdin.readlines()]

def dfs(A):
  if len(A)==N:
    print(*A)
    return
  if len(A)==0:
    start=1
  else:
    start=A[-1]+1
  for i in range(start,M+1):
    dfs(A+[i])
 
# N,M=map(int,input().split())
dfs([])