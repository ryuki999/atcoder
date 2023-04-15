N = int(input())
S = input()

more = [1] * (len(S) + 1)
more[0] = 1
for i in range(len(S)):
    if S[i] == "A":
        more[i + 1] = max(more[i] + 1, 1)
# print(more)

less = [1] * (len(S) + 1)
less[len(S)] = 1
for i in reversed(range(len(S))):
    if S[i] == "B":
        less[i] = max(less[i + 1] + 1, 1)

# print(less)

dp = [0] * (len(S) + 1)
for i in range(N):
    dp[i] = max(more[i], less[i])

print(sum(dp))
