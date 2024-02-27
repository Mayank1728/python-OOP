# perfect number
def is_perfect_number(num):
    sum_ = 0
    for i in range(1, num):
        if num % i == 0:
            sum_ += i
    return sum_ == num


ans = is_perfect_number(6)
print(ans)
