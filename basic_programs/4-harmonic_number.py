# harmonic value
add_all = 0
num = 10
if num <= 0:
    print("Invalid Input")
else:
    start = 1
    while num:
        add_all += 1 / start
        num = num - 1
        start = start + 1
    print("Sum: ", add_all)
