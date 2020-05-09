# Python program for implementation of QuickSort
# This fuction takes last element as pivot places
# The pivot element at its correct position in sorted
# Array and Places all smaller(smaller than pivot)
# To left to pivot and all greater elements to right
# of pivot

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


# The main function that implements QuickSort
# arr[] --> Array to be sorted
# low --> Starting index
# high --> Ending index

# Function to be QuickSort
def quick_sort(arr, low, high):
    if low < high:
        # pi is partitioning index, arr[p] is now
        # At right place
        pi = partition(arr, low, high)

        # Separetly sort elements before
        # Partition and after partition
        quick_sort(arr, low, pi - 1)
        quick_sort(arr, pi + 1, high)

    # Driver code to test above


arr = [10, 7, 8, 9, 1, 5, 0, 100]
n = len(arr)
quick_sort(arr, 0, n - 1)
print("Sorted array is:")
for i in range(n):
    print("%d"%arr[i])