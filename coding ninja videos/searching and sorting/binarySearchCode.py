def binarySearch(arr, element):
    start = 0
    end = len(arr)-1
    while (start <= end):
        mid = (start+end)//2

        if (arr[mid] == element):
            return mid
        elif (arr[mid] < element):
            start = mid+1
        else:
            end = mid-1
    return -1


array = [1, 3, 6, 7, 14, 24, 66, 88, 89, 266, 366, 567, 788, 899]
index = binarySearch(array, 266)
print(index)
