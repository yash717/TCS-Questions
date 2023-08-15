def bubbleSort(arr):
    length = len(arr)
    for i in range(length-1):
        for j in range(length-1-i):
            if (arr[j] > arr[j+1]):
                arr[j], arr[j+1] = arr[j+1], arr[j]


array = [234, 23, 2524, 56, 234, 235, 346, 35234423,
         34, 63452, 4, 346, 345, 245, 246, 36, 34, 5]
bubbleSort(array)
print(array)
