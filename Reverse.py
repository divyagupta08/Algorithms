array = [1, 2, 3, 4, 5, 6, 7, 8, 9]

n = len(array)
for i in range(0, int(n / 2)):
    array[i], array[n - i - 1] = array[n - i - 1], array[i]

print(array)