# N, M = map(int, input().split())
S = input()
# A = list(map(int, input().split()))
# A = [i.strip() for i in sys.stdin.readlines()]

youbi = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]
 
for i, s in enumerate(youbi):
  if S == s:
    break

print(5-i)