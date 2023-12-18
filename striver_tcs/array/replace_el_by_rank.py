def replaceByRank(arr):
    n = len(arr)
    sorted_arr = sorted(arr)
    hashmap = {}

    for i, val in enumerate(sorted_arr):
        hashmap[val] = i+1

    for i in range(n):
        arr[i] = hashmap[arr[i]]

    return arr


def replaceByRank(arr):
    sorted_arr = sorted(arr)  # Sort the array to obtain ranks
    rank_dict = {}  # Initialize an empty dictionary to store element-rank pairs

    # Create element-rank dictionary
    for i, val in enumerate(sorted_arr):
        # Assign each element from sorted_arr its corresponding rank
        rank_dict[val] = i + 1

    # Replace elements in the array by their ranks using the dictionary
    for i in range(len(arr)):
        # Replace each element in arr with its rank from rank_dict
        arr[i] = rank_dict[arr[i]]

    return arr  # Return the array with elements replaced by their ranks


# Test Cases
arr1 = [20, 15, 26, 2, 98, 6]
result1 = replaceByRank(arr1)
print("Example 1:")
print("Input:", arr1)
print("Output:", result1)

arr2 = [1, 5, 8, 15, 8, 25, 9]
result2 = replaceByRank(arr2)
print("\nExample 2:")
print("Input:", arr2)
print("Output:", result2)

arr = [3, 43, 5, 64, 6234, 6, 342, 45,
       24652, 4656, 45, 345, 6, 36, 3456, 35, 6]
print(replaceByRank(arr))
