# Solution 1: Use of two loops

def countFreq(arr, n):
    visited = [False]*n
    for i in range(n):
        if visited[i] == True:
            continue
        count = 1

        for j in range(i+1, n):
            if arr[i] == arr[j]:
                visited[j] = True
                count += 1
        print(arr[i], count)

# Solution 2: Using Map


def countFreq2(arr, n):
    occurrences = {}
    for i in arr:
        if i in occurrences:
            occurrences[i] += 1
        else:
            occurrences[i] = 1

    for j in occurrences:
        print(j, occurrences[j])


if __name__ == '__main__':
    arr = [10, 5, 10, 15, 10, 5]
    n = len(arr)
    countFreq2(arr, n)
