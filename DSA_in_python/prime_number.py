def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, n):
        if n % i == 0:
            print("Number is divisible by", i)
            return False
    return True


ans = is_prime(14)
print(ans)
