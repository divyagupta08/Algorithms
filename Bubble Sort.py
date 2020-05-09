def bubble_sort(arr):
    arr_len = len(arr)
    #print(arr_len)
    total_iteration = 0
    for outer_index in range(arr_len-1):
        #print("outer index:",outer_index)
        for inner_index in range(arr_len-1-outer_index):
            total_iteration += 1
            #print("inner_index:",inner_index)
            if arr[inner_index]>arr[inner_index+1]:
                arr[inner_index], arr[inner_index+1] = arr[inner_index+1], arr[inner_index]

#arr = [45,16,54,34,5,94,36,70,52]
# bubble_sort(arr)
# print(arr)

def bubble_sort_v2(arr):
    arr_len = len(arr)
    #print(arr_len)
    total_iteration = 0
    for outer_index in range(arr_len-1):
        #print("outer index:",outer_index)
        for inner_index in range(arr_len-1):
            total_iteration += 1
            #print("inner_index:",inner_index)
            if arr[inner_index]>arr[inner_index+1]:
                arr[inner_index], arr[inner_index+1] = arr[inner_index+1], arr[inner_index]

#arr = [45,16,54,34,5,94,36,70,52]
# bubble_sort_v2(arr)
# print(arr)

array_1 = [85,23,76,98,12,102,8]
array_2 = [24,27,23,35,34,32,30,35,31,30,32,37,25,36,32,35,36,31,29,26,29,36,20,34,32,29,33,23,31,31,34,27,39,31,30,27,28,38,34,26,25,30,20,20,21,22,30,38,27,26,29,35,31,34,32,20,22,40,26,40,22,22,32,24,38,34,24,36,34,37,28,37,36,37,32,31,30,23,20,39,24,27,24,21,31,28,20,34,38,27,27,32,23,26,25,26,20,24,20,29]

bubble_sort(array_1)
bubble_sort_v2(array_1)

bubble_sort(array_2)
bubble_sort_v2(array_2)

print(array_1)
print(array_2)