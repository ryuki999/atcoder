def long_to_base9(n):
    """10進数から9進数へ変換
    s8 = long_to_base9("894")
    """
    ans = ""
    while n > 0:
        c = str(n % 9)
        ans = c + ans
        n //= 9
    if ans == "":
        return "0"
    return ans
