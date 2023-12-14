def findSymmetricPairs(arr):
    pair_dict = {}
    symmetric_dict = []

    for pair in arr:
        first, second = pair

        if (second, first) in pair_dict:
            symmetric_dict.append(pair)
            symmetric_dict.append((second, first))

        pair_dict[pair] = True

    return symmetric_dict


# Example 1
arr1 = [(1, 2), (2, 1), (3, 4), (4, 5), (5, 4)]
result1 = findSymmetricPairs(arr1)
print("Example 1:")
print("Output:", result1)

# Example 2
arr2 = [(1, 5), (2, 3), (4, 2), (5, 1), (2, 4)]
result2 = findSymmetricPairs(arr2)
print("\nExample 2:")
print("Output:", result2)
