# Python3 Program for recursive binary search. Return index of x in arr if present, else-1
def binary_search(arr,left,right,key):
    #Check base case
    if right >= left:

        mid = left+(right-left)//2

        #If element is present at the middle itself
        if arr[mid] == key:
            return mid

        #if element is smaller than mid, then it can be present in left subarray
        elif arr[mid]>key:
            return binary_search(arr,left,mid-1,key)

        #Else the elements can only be present in right subarray
        else:
            return binary_search(arr,mid+1,right,key)

    else:
        #Elements is not present in the array
        return-1

#Driver Code
arr = [2,3,4,10,40]
x = 10

#Function call
result = binary_search(arr,0,len(arr)-1,x)

if result !=- 1:
    print("Element is present at index %d"% result )
else:
    print("Elements is not present in array")