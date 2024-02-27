# No of occurences dictionary
occurs = {}
arr = [34, 23, 45, 34, 1, 0, 0, 0, -2, 0]
for _, val in enumerate(arr):
    if val in occurs:
        occurs[val] += 1
    else:
        occurs[val] = 1

print(occurs)
