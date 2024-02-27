# remove first occurence
# I am replacing 
# Linear search
arr = [2, 34, 9, 78, -3, 23, 9]
rem = 9
for i, val in enumerate(arr):
    if val == rem:
        arr[i] = -1
        break

print(arr)
