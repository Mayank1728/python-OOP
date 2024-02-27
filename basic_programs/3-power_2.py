# power of 2

power = 5
if power < 0:
    print("Invalid input")
else:
    max_val = 2 ** power
    start = 1
    while start <= max_val:
        print(start)
        start = start * 2

print("Finished")
