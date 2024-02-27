# reverse

arr = [10, -20, 30, 40]
start, end = 0, len(arr) - 1
while start <= end:
    temp = arr[start]
    arr[start] = arr[end]
    arr[end] = temp
    start += 1
    end -= 1

for i in range(len(arr)):
    print(arr[i])

# using function
print(arr[::-1])
