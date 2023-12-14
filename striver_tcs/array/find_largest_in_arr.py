
#brute force
def find_largest(arr, n):
    arr.sort()
    return arr[n-1]

#optimal

def find_largest_2(arr,n):
    largest=arr[0]
    for i in arr:
        if largest<i:
            largest=i
            
    return largest
        



arr1 = [2, 5, 1, 3, 0]
arr2 = [8, 10, 5, 7, 9]
n=5
print("The Largest element in the array is:", find_largest_2(arr1,n))
print("The Largest element in the array is:", find_largest_2(arr2,n))
