#mylist = [54, 23, 93, 17, 77, 31, 44, 55, 20]
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


mylist = [54, 23, 93, 17, 77, 31, 44, 55, 20]

merge_sort(mylist)
print("Merging", mylist)