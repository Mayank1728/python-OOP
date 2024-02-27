import random


def generate_copuns(n):
    s = set()
    while True:
        if len(s) >= n:
            break
        rand_num = random.randint(1, 10 * n)
        if rand_num not in s:
            s.add(rand_num)
    return list(s)


num = 100
res = generate_copuns(num)
print(res)
