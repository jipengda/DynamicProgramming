def F(n):
    if n == 0 or n == 1:
        return n
    else:
        return F(n-1)+F(n-2)
