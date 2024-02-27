from random import randint

no_of_times_flip = 10

print("Lets start Flipping: ")
for i in range(0, no_of_times_flip):
    flip_res = randint(0, 1)
    if flip_res == 0:
        print("Head")
    else:
        print("Tails")
