def parlindrome(arr):
    n = len(arr)
    for i in range(0,n//2):
        if arr[i] != arr[n-i-1]:
            return False
    return True

arr = [1,2,3,4,2,1]

result = parlindrome(arr)
print(result)