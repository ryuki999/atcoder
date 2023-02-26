# 全探索

N = int(input())

def hantei(t):
    dep = 0
    for i in range(len(t)):
        if t[i] == "(":
            dep += 1
        if t[i] == ")":
            dep -= 1
        if dep < 0:
            return False
    if dep == 0:
        return True
    return False

for i in range(2**N):
    t = ""
    for j in range(N-1, -1, -1):
        """1を立てたところと一致してたら), そうでなければ(
        i=3, j=3, 3(011)&1000
        i=3, j=2, 3(011)&0100
        i=3, j=1, 3(011)&0010
        i=3, j=0, 3(011)&0001
        """
        if (i &(1 << j)) == 0:
            t += "("
        else:
            t += ")"
    if hantei(t):
        print(t)