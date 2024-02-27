# find prime numbers

prime_numbers = set()


def is_prime(num) -> bool:
    if num in prime_numbers:
        return True
    total_factors = 0
    for i in range(2, num + 1):
        if total_factors > 2:
            break
        if num % i == 0:
            total_factors += 1
    if total_factors <= 2:
        prime_numbers.add(num)
    return total_factors <= 2


num = 1001
print("Prime factors of", num)
for i in range(2, num + 1):
    if is_prime(i) and num % i == 0:
        print(i)