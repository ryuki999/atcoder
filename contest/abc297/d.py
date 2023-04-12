A, B = map(int, input().split())

ans = 0
while A != B:
    if A>B:
        if A%B ==0:
            ans +=A//B-1
            A =B
        else:
            ans +=  A//B
            A=A%B
        # print(A,B, A%B,ans)
        # print(A,B, A%B, ans)
        continue
    if A<B:
        if B%A ==0:
            ans +=B//A-1
            B =A
        else:
            ans += B//A
            B=B%A
        # print(A,B, B%A,ans)
        # print(A,B, B%A, ans)
        continue
print(ans)

