def sortByFrequency(arr):
    # Initialize an empty dictionary to store element frequencies
    freq_dict = {}

    # Loop through each element in the input array
    for element in arr:
        # Check if the element is already in the frequency dictionary
        if element in freq_dict:
            # If the element exists, increment its frequency count
            freq_dict[element] += 1
        else:
            # If the element doesn't exist, initialize its frequency count to 1
            freq_dict[element] = 1

    # Define a custom sorting function based on frequencies and values
    def custom_sort(x):
        # Sort elements in descending order of frequency, then ascending order of values
        return (-freq_dict[x], x)

    # Sort the input array based on the custom sort function
    arr.sort(key=custom_sort)

    # Return the sorted array
    return arr


# Test cases
arr1 = [1, 2, 3, 2, 4, 3, 1, 2]
result1 = sortByFrequency(arr1)
print("Example 1:")
print("Input:", arr1)
print("Output:", result1)

arr2 = [-199, 6, 7, -199, 3, 5]
result2 = sortByFrequency(arr2)
print("\nExample 2:")
print("Input:", arr2)
print("Output:", result2)
