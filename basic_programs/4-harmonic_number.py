# harmonic value
sum = 0
num = 10
if num <= 0:
    print("Invalid Input")
else:
    start = 1
    while num:
        sum += 1 / start
        num = num - 1
        start = start + 1
    print("Sum: ", sum)
