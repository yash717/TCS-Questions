def selectionSort(arr):
    length = len(arr)
    for i in range(length-1):
        minIndex = i
        for j in range(i+1, length):
            if (arr[j] < arr[minIndex]):
                minIndex = j
        arr[i],  arr[minIndex] = arr[minIndex], arr[i]


array = [234, 23, 2524, 56, 234, 235, 346, 35234423,
         34, 63452, 4, 346, 345, 245, 246, 36, 34, 5]
selectionSort(array)
print(array)
