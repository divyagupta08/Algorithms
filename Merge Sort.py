def merge_sort(mylist):
    if len(mylist) > 1:
        mid = len(mylist) // 2
        lefthalf = mylist[:mid]
        righthalf = mylist[mid:]

        # Recursive call on each half
        merge_sort(lefthalf)
        merge_sort(righthalf)

        # Two iteration for traversing the two halves
        i = 0
        j = 0

        # Itration for the main list
        k = 0

        while i < len(lefthalf) and j < len(righthalf):
            if lefthalf[i] < righthalf[j]:
                # The value from the left half has been used
                mylist[k] = lefthalf[i]
                # Move the iterator forward
                i += 1
            else:
                mylist[k] = righthalf[j]
                j += 1
            # Move to the next slot
            k += 1

        # For all the remaining values
        while i < len(lefthalf):
            mylist[k] = lefthalf[i]
            i += 1
            k += 1

        while j < len(righthalf):
            mylist[k] = righthalf[j]
            j += 1
            k += 1


mylist = [54, 23, 93, 17, 77, 31, 44, 55, 20]              #Output: Merging [17, 20, 23, 31, 44, 54, 55, 77, 93]
#mylist = [25,4,17,31,3,56,40,8,68,98,82,79]                #Output: Merging [3, 4, 8, 17, 25, 31, 40, 56, 68, 79, 82, 98]
#mylist = [5,56,-3,42,15,0,74,-38,-34]                      #Output: Merging [-38, -34, -3, 0, 5, 15, 42, 56, 74]
#mylist = [-5,-78,-20,-68,-47,-36,-8,-17,-98,-55]           #Output:  Merging [-98, -78, -68, -55, -47, -36, -20, -17, -8, -5]
#mylist = [56.38,42.8,7.54,39,42.21,98,2.22]                #Output: Merging [2.22, 7.54, 39, 42.21, 42.8, 56.38, 98]
#mylist = [34,12,-5,20,96,45,-10,87,29,-57,-3,75,36,-8]     #Output: Merging [-57, -10, -8, -5, -3, 12, 20, 29, 34, 36, 45, 75, 87, 96]

merge_sort(mylist)
print("Merging", mylist)









# #Merge two sorted arrays
def merge_arrays(arr1, arr2, n1, n2):
    arr3 = [None] * (n1 + n2)
    i = 0
    j = 0
    k = 0

    # Transverse both array
    while i < n1 and j < n2:

        # Check if current elements of first array is smaller than current element of second array.
        # If yes, store first array element and increment first array index. Otherwise do same with second array
        if arr1[i] < arr2[j]:
            arr3[k] = arr1[i]
            k += 1
            i += 1
        else:
            arr3[k] = arr2[j]
            k += 1
            j += 1

    # Store remaining elements
    # of first array
    while i < n1:
        arr3[k] = arr1[i]
        k += 1
        i += 1

    # Store remaining elements
    # of second array
    while j < n2:
        arr3[k] = arr2[j]
        k += 1
        j += 1

    print("Array after merging")
    for i in range(n1 + n2):
        print(str(arr3[i]))


# Divide Code
arr1 = [1, 3, 5, 7]
arr2 = [2, 4, 6, 8]              #Output: Array after merging [1,2,3,4,5,6,7,8]

# arr1 = [1, 3, 5, 7, 9]
# arr2 = [2, 4, 6, 8, 10]          #Output: Array after merging [1,2,3,4,5,6,7,8,9,10]

# arr1 = [11, 13, 15, 17, 19]
# arr2 = [2, 4, 6, 8]              #Output: Array after merging [2,4,6,8,11,13,15,17,19]

# arr1 = [1]
# arr2 = [2, 4, 6, 8, 10]            #Output: Array after merging [1,2,4,6,8,10]

# arr1 = [-3, -1, 5, 7, 9]
# arr2 = [ -4, 6]                    #Output: Array after merging [-4,-3,-1,5,6,7,9]

# arr1 = [-98,-24,-19,-8,-3, -1]
# arr2 = [ -21]                       #Output: Array after merging [-98,-24,-21,-19,-8,-3,-1]


n1 = len(arr1)
n2 = len(arr2)

merge_arrays(arr1, arr2, n1, n2)