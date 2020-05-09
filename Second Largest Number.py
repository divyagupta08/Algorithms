# Python program to find second one number in a array

# Array of numbers - Length of array should be at least 2
# array = [21,85,67,45,3,50,37,10,94,28]
#
# mx = max(array[0], array[1])
# secondmax = min(array[0], array[1])
# n = len(array)
#
# for i in range(2, n):
#     if array[i] > mx:
#         secondmax = mx
#         mx = array[i]
#     elif array[i] > secondmax and mx != array[i]:
#         secondmax = array[i]
#     else:
#         if secondmax == mx:
#             secondmax = array[i]

#print("Second highest number is:", str(secondmax))



# arr = [17, 62, 45, 3, 50, 37, 62, 94, 85, 28]
# mx = arr[0]
# secondmax = arr[0]
# n = len(arr)
#
# for i in range(1, n):
#     if mx < arr[i]:
#         mx = arr[i]
#     else:
#         mx = mx
#
#     for j in range(1, n):
#         if arr[j]<mx:
#             if secondmax < arr[j]:
#                 secondmax = arr[j]
#             else:
#                 secondmax = secondmax
#
# print("Second largest number:", secondmax)
# print("Largest number:", mx)



#arr = [17, 62, 45, 3, 50, 37, 62, 94, 85, 28]
#arr = [-1,-2,-3,-4,-5]
#arr = [5,5,5,5,5]
#arr = [5]
arr = [2,-1,-2,-3,4,-4,-5]
def second_highest(arr):
    if len(arr)<2:
        return "No elements found"

    if arr[0]>arr[1]:
        first = arr[0]
        second = arr[1]
    else:
        second = arr[0]
        first = arr[1]

    for i in range(2,len(arr)):
        if arr[i]>first:
            second = first
            first = arr[i]
        elif second<arr[i]<first:
            second = first
        else:
            pass

        return second
result = second_highest(arr)
print(result)