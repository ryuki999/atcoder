L, R = map(int, input().split(" "))
S = input()

text = ""
text += S[:L-1]

text += S[L-1:R][::-1]
text += S[R:]

        
print(text)
