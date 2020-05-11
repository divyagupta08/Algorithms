# Find Median of two sorted array with the felp of Merge Sort

# def get_median(arr1, arr2):
#     arr3 = [None] * (len(arr1) + len(arr2))
#     i, j, k = 0, 0, 0
#
#     while i < len(arr1) and j < len(arr2):
#         if arr1[i] < arr2[j]:
#             arr3[k] = arr1[i]
#             i += 1
#             k += 1
#         else:
#             arr3[k] = arr2[j]
#             j += 1
#             k += 1
#
#     while i < len(arr1):
#         arr3[k] = arr1[i]
#         i += 1
#         k += 1
#
#     while j < len(arr2):
#         arr3[k] = arr2[j]
#         j += 1
#         k += 1
#
#     mid = len(arr3) // 2
#     if len(arr3) % 2 == 1:  # If len(arr3) is odd
#         median = arr3[mid]
#     else:  # If len(arr3) is even
#         median = (arr3[mid] + arr3[mid - 1]) / 2
#
#     return median


# arr1 = [1,12,15,26,38]
# arr2 = [2,13,17,30,45]   #Median = 16

# arr1 = [1,12,15,26,38,65]
# arr2 = [2,13,17,30,45,53]  #Median = 21.5

# arr1 = [1,12,15,26,38,65]
# arr2 = [2,13,17,30,45,53,71,99]  #Median = 28

# arr1 = [1, 5, 17, 33, 50, 61]
# arr2 = [2, 4, 8, 15, 42, 65]  # Median = 16

# result = get_median(arr1, arr2)
# print(result)




# Find the median with the help of using Divide and Conquer rule

def get_median_v2(arr1, arr2, n):
    if n == 1:
        return (arr1[0] + arr2[0]) / 2

    elif n == 2:
        return (min(arr1[1], arr2[1]) + max(arr1[0], arr2[0])) / 2

    else:
        m1 = median(arr1, n)
        m2 = median(arr2, n)

        if m1 > m2:
            if n % 2 == 0:
                return get_median_v2(arr1[:(n // 2) + 1], arr2[(n // 2) - 1:], (n // 2) + 1)
            else:
                return get_median_v2(arr1[:(n // 2) + 1], arr2[(n // 2):], (n // 2) + 1)

        else:
            if n % 2 == 0:
                return get_median_v2(arr1[(n // 2 - 1):], arr2[:(n // 2) + 1], (n // 2) + 1)
            else:
                return get_median_v2(arr1[(n // 2):], arr2[:(n // 2) + 1], (n // 2) + 1)


def median(arr, n):
    if n % 2 == 0:
        return (arr[n // 2] + arr[(n // 2) - 1]) / 2
    else:
        return arr[n // 2]


# arr1 = [1, 12, 15, 26, 38]
# arr2 = [2, 13, 17, 30, 45]  #Median = 16

# arr1 = [1,12,15,26,38,65]
# arr2 = [2,13,17,30,45,98]  #Median = 21.5

# arr1 = [1,12,15,26,38,65]
# arr2 = [2,13,17,30,45,53,71,99]  #Median = 21.5 (Length of both the arrays are not equal so it gives wrong output)

arr1 = [1, 5, 17, 33, 50, 61]
arr2 = [2, 4, 8, 15, 42, 65]  # Median = 16

n = len(arr1)

result = get_median_v2(arr1, arr2, n)
print(result)