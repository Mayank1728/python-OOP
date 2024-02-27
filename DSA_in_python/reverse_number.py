def reverse_num(n):
    rn = 0
    while n:
        rn = rn * 10 + (n % 10)
        n = n // 10
    return rn


rev = reverse_num(9989977)
print(rev)
