arr = [14, 33, 27, 10, 35, 19, 42, 44]

for i in range(len(arr)):
    index_min = i
    for j in range(i + 1, len(arr)):
        if arr[j] < arr[index_min]:
            index_min = j
    arr[i], arr[index_min] = arr[index_min], arr[i]

print(arr)
