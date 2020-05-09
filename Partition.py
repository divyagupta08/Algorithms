def partition(arr, low, high):
    i = (low - 1)  # Index of smaller element
    pivot = arr[high]  # Pivot

    for j in range(low, high):

        # If current element is smaller than the pivot
        if arr[j] < pivot:
            # Increment index of smaller element
            i += 1
            arr[i], arr[j] = arr[j], arr[i]

    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return (i + 1)


arr = [10, 7, 8, 9, 1, 5, 0, 100]
n = len(arr)
partition_index = partition(arr, 0, n - 1)
print(partition_index)