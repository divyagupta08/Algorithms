array = [1, 2, 3, 4, 5, 6, 7, 8, 9]
#array = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

def reverse(array):
    n = len(array)
    for i in range(0, int(n // 2)):
        array[i], array[n - i - 1] = array[n - i - 1], array[i]

reverse(array)
print(array)



def reverse_1(array):
    destination_arr = []
    n = len(array)
    for i in reversed(range (n)):
        print(i)
        destination_arr.append(array [i])
    print(destination_arr)
    pass

reverse_1(array)
